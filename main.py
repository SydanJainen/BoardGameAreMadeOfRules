#!/usr/bin/env python3

import json
import sys
import argparse
from pathlib import Path

from src.core.models import Audience, RawContent
from src.core.llm import LocalModelRegistry, validate_ollama_config
from src.core.adapters import (
    PDFAdapter, PdfPlumberAdapter, TablePDFAdapter, OCRPDFAdapter, ImagePDFAdapter,
    TextAdapter, InlineAdapter, ConceptAdapter, BGGAdapter,
)
from src.core.utils import (
    TextCleaner,
    UnifiedParser,
    JSONFormatter,
    MarkdownFormatter,
    load_config,
)
from src.prompts import (
    AnalysePrompt,
    ExplainPrompt,
    FixRulesPrompt,
    InventPrompt,
    MovePrompt,
)
from src.pipelines import (
    ExplainPipeline,
    AnalysePipeline,
    FixRulesPipeline,
    InventPipeline,
    MovePipeline,
)


def main():

    parser = argparse.ArgumentParser(
        description="LLM-based boardgame rules analyser using clean architecture",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("--template", help="Load configuration from template file")
    parser.add_argument("--model", help="Model to use (alias from config)")

    # Common arguments shared by all subcommands
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--model", help="Model to use (alias from config)")
    common.add_argument("--output", help="Output file path (JSON or MD)")
    common.add_argument("--format", choices=["json", "markdown"], default="markdown")
    common.add_argument(
        "--pdf-mode",
        choices=["basic", "plumber", "ocr", "tables", "images"],
        default="basic",
        help="PDF extraction method (default: basic PyPDF2)",
    )

    subparsers = parser.add_subparsers(dest="command", help="Task to perform")

    # EXPLAIN task
    explain_parser = subparsers.add_parser("explain", parents=[common], help="Explain rules to different audiences (child/adult/expert)")
    explain_parser.add_argument("--input", required=True, help="Path to rulebook (PDF or TXT)")
    explain_parser.add_argument(
        "--audience",
        choices=["child", "adult", "expert"],
        default="adult",
        help="Target audience",
    )

    # ANALYSE task
    analyse_parser = subparsers.add_parser("analyse", parents=[common], help="Extract game properties and compare with BoardGameGeek")
    analyse_parser.add_argument("--input", help="Path to rulebook (PDF or TXT)")
    analyse_parser.add_argument("--bgg-id", type=int, help="BoardGameGeek game ID for comparison")
    analyse_parser.add_argument("--bgg-name", type=str, help="BoardGameGeek game name for comparison (alternative to --bgg-id)")

    # FIX-RULES task
    fix_parser = subparsers.add_parser("fix-rules", parents=[common], help="Identify missing or flawed rules and suggest corrections")
    fix_parser.add_argument("--input", required=True, help="Path to rulebook (PDF or TXT)")

    # INVENT task
    invent_parser = subparsers.add_parser("invent", parents=[common], help="Invent a new boardgame based on a concept or theme")
    invent_parser.add_argument("--concept", required=False, help="Game concept or theme description")
    invent_parser.add_argument("--wizard", action="store_true", help="Launch interactive wizard to create template")
    invent_parser.add_argument("--theme", help="Specific theme (optional)")
    invent_parser.add_argument("--mechanics", help="Preferred mechanics (optional)")

    # RECOMMEND-MOVE task
    move_parser = subparsers.add_parser("recommend-move", parents=[common], help="Recommend the next move given rules and game state")
    move_parser.add_argument("--rules", required=True, help="Path to rulebook (PDF or TXT)")
    move_parser.add_argument("--state", required=True, help="Current game state description")

    args = parser.parse_args()

    if args.template:
        if not hasattr(args, "model"):
            args.model = None
        execute_from_template(args)
        return

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        if args.command == "explain":
            execute_explain(args)
        elif args.command == "analyse":
            execute_analyse(args)
        elif args.command == "fix-rules":
            execute_fix_rules(args)
        elif args.command == "invent":
            execute_invent(args)
        elif args.command == "recommend-move":
            execute_recommend_move(args)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def setup_registry(config_path="config/config.json"):
    config = load_config(config_path)
    ollama_config = config.get("ollama", {})
    validate_ollama_config(ollama_config)
    return LocalModelRegistry(ollama_config), config


def _resolve_model(registry, model_alias=None):
    if model_alias:
        client = registry.get_model(model_alias)
        if client is None:
            available = ", ".join(m.alias for m in registry.get_all_models())
            raise ValueError(f"Model '{model_alias}' not found. Available: {available}")
        return client
    return registry.get_default_model()


def _create_file_adapter(file_path, pdf_mode="basic"):
    path = Path(file_path)
    if path.suffix.lower() == ".pdf":
        if pdf_mode == "plumber":
            return PdfPlumberAdapter(file_path)
        elif pdf_mode == "ocr":
            return OCRPDFAdapter(file_path)
        elif pdf_mode == "tables":
            return TablePDFAdapter(file_path, output_dir="results/extracted")
        elif pdf_mode == "images":
            return ImagePDFAdapter(file_path)
        else:
            return PDFAdapter(file_path)
    elif path.suffix.lower() in [".txt", ".md"]:
        return TextAdapter(file_path)
    else:
        raise ValueError(f"Unsupported file type: {path.suffix}")


def _create_bgg_adapter(config, bgg_id=None, bgg_name=None):
    if not bgg_id and not bgg_name:
        return None
    bgg_config = config.get("bgg", {})
    return BGGAdapter(
        game_id=bgg_id,
        game_name=bgg_name,
        api_token=bgg_config.get("api_token"),
        cache_dir=bgg_config.get("cache_dir", "cache/bgg"),
        cache_expiry_days=bgg_config.get("cache_expiry_days", 30),
        rate_limit_seconds=bgg_config.get("rate_limit_seconds", 5.0),
    )


def output_result(result, output_path, format_type):
    if output_path:
        if format_type == "json":
            JSONFormatter.save(result, output_path)
        else:
            MarkdownFormatter.save(result, output_path)
        print(f"Saved to: {output_path}")
    else:
        if format_type == "json":
            print("\n" + JSONFormatter.format(result))
        else:
            print("\n" + MarkdownFormatter.format(result))


def execute_explain(args):
    registry, config = setup_registry()
    llm_client = _resolve_model(registry, args.model)

    pipeline = ExplainPipeline(
        data_adapter=_create_file_adapter(args.input, getattr(args, "pdf_mode", "basic")),
        llm_client=llm_client,
        prompt_strategy=ExplainPrompt(),
        preprocessor=TextCleaner(),
    )
    result = pipeline.execute(audience=Audience(args.audience))

    output_result(result, args.output, args.format)
    print("\nExplanation generated successfully!")


def execute_analyse(args):
    if not args.input and not args.bgg_id and not args.bgg_name:
        print("Error: At least one of --input, --bgg-id, or --bgg-name must be provided", file=sys.stderr)
        sys.exit(1)

    if args.bgg_id and args.bgg_name:
        print("Error: Cannot be both --bgg-id and --bgg-name", file=sys.stderr)
        sys.exit(1)

    print("Analysing game properties...")
    if args.input:
        print(f"Input: {args.input}")
    if args.bgg_id:
        print(f"BGG comparison: Game ID {args.bgg_id}")
    if args.bgg_name:
        print(f"BGG comparison: Game name '{args.bgg_name}'")

    registry, config = setup_registry()
    llm_client = _resolve_model(registry, args.model)
    bgg_adapter = _create_bgg_adapter(config, bgg_id=args.bgg_id, bgg_name=args.bgg_name)

    data_adapter = _create_file_adapter(args.input, getattr(args, "pdf_mode", "basic")) if args.input else None

    pipeline = AnalysePipeline(
        data_adapter=data_adapter,
        llm_client=llm_client,
        prompt_strategy=AnalysePrompt(),
        preprocessor=TextCleaner(),
        bgg_adapter=bgg_adapter,
    )
    result = pipeline.execute()

    output_result(result, args.output, args.format)

    if args.input:
        print("\nAnalysis completed successfully!")
        print(f"\nMechanics: {', '.join(result.mechanics)}")
        print(f"Complexity: {result.complexity}/5.0")
        print(f"Players: {result.min_players}-{result.max_players}")
        print(f"Duration: {result.duration_min} minutes")

        if result.overall_score:
            print(f"\nOverall BGG Match Score: {result.overall_score:.1%}")
    else:
        print("\nBGG data fetched successfully!")
        print(f"\nMechanics: {', '.join(result.bgg_mechanics)}")
        print(f"Complexity: {result.bgg_complexity}/5.0")
        print(f"Players: {result.bgg_players}")
        print(f"Duration: {result.bgg_duration} minutes")


def execute_fix_rules(args):
    print("Analysing rules for issues...")
    print(f"Input: {args.input}")

    registry, config = setup_registry()
    llm_client = _resolve_model(registry, args.model)

    pipeline = FixRulesPipeline(
        data_adapter=_create_file_adapter(args.input, getattr(args, "pdf_mode", "basic")),
        llm_client=llm_client,
        prompt_strategy=FixRulesPrompt(),
        preprocessor=TextCleaner(),
    )
    result = pipeline.execute()

    output_result(result, args.output, args.format)
    print("\nRule analysis completed successfully!")
    print(f"\nIdentified {len(result.identified_issues)} issue(s)")


def execute_invent(args):
    if args.wizard:
        from src.wizard import InventWizard

        wizard = InventWizard()
        template_path, should_execute = wizard.run()
        if should_execute:
            args.template = template_path
            execute_from_template(args)
        return

    if not args.concept:
        print("Error: --concept is required when not using --wizard", file=sys.stderr)
        sys.exit(1)

    print("Inventing new boardgame...")
    print(f"Concept: {args.concept}")

    registry, config = setup_registry()
    llm_client = _resolve_model(registry, args.model)

    pipeline = InventPipeline(
        data_adapter=ConceptAdapter(args.concept),
        llm_client=llm_client,
        prompt_strategy=InventPrompt(),
        preprocessor=None,
        response_parser=UnifiedParser(),
    )
    result = pipeline.execute(
        theme=args.theme or "", mechanics=args.mechanics or ""
    )

    output_result(result, args.output, args.format)
    print("\nGame invented successfully!")
    print(f"\nGame Name: {result.game_name}")
    print(f"Mechanics: {', '.join(result.mechanics)}")


def execute_recommend_move(args):
    print("Recommending move...")
    print(f"Rules: {args.rules}")
    print(f"State: {args.state[:100]}...")

    registry, config = setup_registry()
    llm_client = _resolve_model(registry, args.model)

    pipeline = MovePipeline(
        data_adapter=_create_file_adapter(args.rules, getattr(args, "pdf_mode", "basic")),
        llm_client=llm_client,
        prompt_strategy=MovePrompt(),
        preprocessor=TextCleaner(),
    )
    result = pipeline.execute(game_state=args.state)

    output_result(result, args.output, args.format)
    print("\nMove recommendation generated successfully!")
    print(f"\nRecommended: {result.recommended_move}")


def _create_adapter_from_template(command, content, pdf_mode="basic"):
    if command == "invent":
        concept_text = content.get("idea_summary") or content.get("concept", "")
        if not concept_text:
            raise ValueError("Template must specify 'idea_summary' or 'concept' in content")
        return ConceptAdapter(concept_text)

    if "rules_file" in content:
        return _create_file_adapter(content["rules_file"], pdf_mode)
    elif "rules" in content:
        return InlineAdapter(content["rules"], metadata={"source": "template"})
    else:
        raise ValueError("Template must specify 'rules' or 'rules_file' in content")


def execute_from_template(args):
    from src.core.templates import TemplateLoader

    print(f"Loading template: {args.template}")

    try:
        template = TemplateLoader.load(args.template)

        registry, config = setup_registry()
        effective_model = args.model or template.model
        llm_client = _resolve_model(registry, effective_model if effective_model else None)

        params = template.parameters
        content = template.content
        output_path = params.get("output_file")
        output_format = params.get("format", "markdown")

        template_pdf_mode = params.get("pdf_mode", "basic")
        data_adapter = _create_adapter_from_template(template.command, content, template_pdf_mode)

        if template.command == "explain":
            audience = Audience(params.get("audience", "adult"))
            pipeline = ExplainPipeline(
                data_adapter=data_adapter,
                llm_client=llm_client,
                prompt_strategy=ExplainPrompt(),
                preprocessor=TextCleaner(),
            )
            result = pipeline.execute(audience=audience)
            output_result(result, output_path, output_format)
            print("\nExplanation generated successfully!")

        elif template.command == "analyse":
            bgg_adapter = _create_bgg_adapter(
                config,
                bgg_id=params.get("bgg_id"),
                bgg_name=params.get("bgg_name"),
            )
            pipeline = AnalysePipeline(
                data_adapter=data_adapter,
                llm_client=llm_client,
                prompt_strategy=AnalysePrompt(),
                preprocessor=TextCleaner(),
                bgg_adapter=bgg_adapter,
            )
            result = pipeline.execute()
            output_result(result, output_path, output_format)
            print("\nAnalysis completed successfully!")
            print(f"\nMechanics: {', '.join(result.mechanics)}")
            print(f"Complexity: {result.complexity}/5.0")
            print(f"Players: {result.min_players}-{result.max_players}")
            print(f"Duration: {result.duration_min} minutes")
            if result.overall_score:
                print(f"\nOverall BGG Match Score: {result.overall_score:.1%}")

        elif template.command == "fix-rules":
            pipeline = FixRulesPipeline(
                data_adapter=data_adapter,
                llm_client=llm_client,
                prompt_strategy=FixRulesPrompt(),
                preprocessor=TextCleaner(),
            )
            result = pipeline.execute()
            output_result(result, output_path, output_format)
            print("\nRule analysis completed successfully!")
            print(f"\nIdentified {len(result.identified_issues)} issue(s)")

        elif template.command == "invent":
            theme = template.context.get("theme", "")
            mechanics = params.get("mechanics", "")
            if isinstance(mechanics, list):
                mechanics = ", ".join(mechanics)

            custom_prompt = template.custom_prompt or ""
            prompt_file = template.prompt_file or ""

            pipeline = InventPipeline(
                data_adapter=data_adapter,
                llm_client=llm_client,
                prompt_strategy=InventPrompt(),
                preprocessor=None,
                response_parser=UnifiedParser(),
            )
            result = pipeline.execute(
                theme=theme, mechanics=mechanics,
                custom_prompt=custom_prompt, prompt_file=prompt_file,
            )
            output_result(result, output_path, output_format)
            print(f"\nGame Name: {result.game_name}")
            print(f"Mechanics: {', '.join(result.mechanics)}")

        elif template.command == "recommend-move":
            game_state = content.get("game_state", "")
            if isinstance(game_state, dict):
                game_state = json.dumps(game_state, indent=2)

            pipeline = MovePipeline(
                data_adapter=data_adapter,
                llm_client=llm_client,
                prompt_strategy=MovePrompt(),
                preprocessor=TextCleaner(),
            )
            result = pipeline.execute(game_state=game_state)
            output_result(result, output_path, output_format)
            print(f"\nRecommended: {result.recommended_move}")

        else:
            print(f"Unknown command in template: {template.command}", file=sys.stderr)
            sys.exit(1)

    except Exception as e:
        print(f"Template execution error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if sys.version_info < (3, 9):
        print("Error: Python 3.9 or higher is required", file=sys.stderr)
        sys.exit(1)

    main()

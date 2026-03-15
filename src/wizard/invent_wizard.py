import os
import sys
from typing import Tuple


class InventWizard:
    AUDIENCES = ["appassionati", "casual", "esperti"]

    def run(self) -> Tuple[str, bool]:
        try:
            print("\n=== Board Game Design Wizard ===")
            print("Crea un nuovo template per inventare un gioco da tavolo.\n")

            # 1. Project name
            project_name = self._ask_required(
                "1. Nome del progetto (usato come nome file)"
            )

            # 2. Target audience
            target = self._ask_choice(
                "2. Target audience",
                self.AUDIENCES,
            )

            # 3. Main mechanics
            mechanics_raw = self._ask_required(
                "3. Meccaniche principali (separate da virgola, es: Worker Placement, Area Control)"
            )
            mechanics = [m.strip() for m in mechanics_raw.split(",") if m.strip()]

            # 4. Complexity
            complexity = self._ask_range(
                "4. Complessita' (1=semplice, 5=molto complesso)", 1, 5
            )

            # 5. Player count (optional - LLM decides if left empty)
            player_count = self._ask_optional(
                "5. Numero giocatori (es. 2-4) [opzionale, invio per lasciare all'LLM]"
            )

            # 6. Duration (optional - LLM decides if left empty)
            duration = self._ask_optional(
                "6. Durata in minuti (es. 60-90) [opzionale, invio per lasciare all'LLM]"
            )

            # 7. Design constraints
            constraints = self._ask_optional(
                "7. Vincoli di design (es. no kingmaking, no player elimination) [opzionale, invio per saltare]"
            )

            # 8. Custom prompt
            print("\n8. Prompt personalizzato (sostituisce il prompt standard)")
            use_custom = self._ask_yes_no(
                "   Vuoi scrivere un prompt personalizzato? [s/n]"
            )
            custom_prompt = ""
            if use_custom:
                custom_prompt = self._ask_multiline(
                    "   Scrivi il prompt (termina con una riga vuota):"
                )

            # 9. Theme
            theme = self._ask_optional(
                "9. Tema (lascia vuoto per farlo proporre all'LLM) [opzionale, invio per saltare]"
            )

            # 10. Inspiration games
            inspiration_raw = self._ask_optional(
                "10. Giochi di ispirazione (separati da virgola) [opzionale, invio per saltare]"
            )
            inspirations = []
            if inspiration_raw:
                inspirations = [g.strip() for g in inspiration_raw.split(",") if g.strip()]

            # 11. Output file path
            default_output = f"results/invent/{project_name}_1.md"
            output_file = self._ask_with_default(
                "11. File di output", default_output
            )

            # Generate template
            template_path = f"templates/invent/{project_name}.md"
            self._write_template(
                template_path=template_path,
                project_name=project_name,
                target=target,
                mechanics=mechanics,
                complexity=complexity,
                player_count=player_count,
                duration=duration,
                constraints=constraints,
                custom_prompt=custom_prompt,
                theme=theme,
                inspirations=inspirations,
                output_file=output_file,
            )

            print(f"\nTemplate salvato in: {template_path}")

            # Ask to execute
            should_execute = self._ask_yes_no("Vuoi eseguirlo subito? [s/n]")

            return (template_path, should_execute)

        except KeyboardInterrupt:
            print("\n\nWizard interrotto. Nessun file creato.")
            sys.exit(0)

    @staticmethod
    def _ask_required(prompt: str) -> str:
        while True:
            value = input(f"{prompt}: ").strip()
            if value:
                return value
            print("  [!] Campo obbligatorio, riprova.")

    @staticmethod
    def _ask_optional(prompt: str) -> str:
        return input(f"{prompt}: ").strip()

    @staticmethod
    def _ask_with_default(prompt: str, default: str) -> str:
        value = input(f"{prompt} [{default}]: ").strip()
        return value if value else default

    @staticmethod
    def _ask_choice(prompt: str, options: list) -> str:
        print(f"{prompt}:")
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")
        while True:
            raw = input("  Scegli (numero): ").strip()
            try:
                idx = int(raw)
                if 1 <= idx <= len(options):
                    return options[idx - 1]
            except ValueError:
                pass
            print(f"  [!] Inserisci un numero tra 1 e {len(options)}.")

    @staticmethod
    def _ask_range(prompt: str, min_val: int, max_val: int) -> int:
        while True:
            raw = input(f"{prompt}: ").strip()
            try:
                val = int(raw)
                if min_val <= val <= max_val:
                    return val
            except ValueError:
                pass
            print(f"  [!] Inserisci un numero intero tra {min_val} e {max_val}.")

    @staticmethod
    def _ask_multiline(prompt: str) -> str:
        print(prompt)
        lines = []
        while True:
            line = input("   > ")
            if not line:
                break
            lines.append(line)
        return "\n".join(lines)

    @staticmethod
    def _ask_yes_no(prompt: str) -> bool:
        while True:
            raw = input(f"{prompt}: ").strip().lower()
            if raw in ("s", "si", "y", "yes"):
                return True
            if raw in ("n", "no"):
                return False
            print("  [!] Rispondi 's' o 'n'.")

    @staticmethod
    def _write_template(
        *,
        template_path: str,
        project_name: str,
        target: str,
        mechanics: list,
        complexity: int,
        player_count: str,
        duration: str,
        constraints: str,
        custom_prompt: str,
        theme: str,
        inspirations: list,
        output_file: str,
    ) -> None:

        # Build mechanics YAML list
        mechanics_yaml = "\n".join(f'    - "{m}"' for m in mechanics)

        # Build inspiration YAML list
        inspiration_yaml = ""
        if inspirations:
            inspiration_yaml = "  inspiration:\n" + "\n".join(
                f'    - "{g}"' for g in inspirations
            )

        # Build custom_prompt block
        custom_prompt_yaml = ""
        if custom_prompt:
            # Indent each line for YAML block scalar
            indented = "\n".join(f"  {line}" for line in custom_prompt.splitlines())
            custom_prompt_yaml = f"custom_prompt: |\n{indented}\n"

        # Build constraints block
        constraints_yaml = ""
        if constraints:
            constraints_yaml = f"  design_constraints: |\n    {constraints}\n"

        # Build the idea summary from all the info
        idea_parts = [f"Un gioco per {target}"]
        if theme:
            idea_parts.append(f"con tema: {theme}")
        idea_parts.append(f"meccaniche: {', '.join(mechanics)}")
        if constraints:
            idea_parts.append(f"vincoli: {constraints}")
        idea_summary = ". ".join(idea_parts) + "."

        # Build optional player_count/duration YAML lines
        player_count_yaml = f'  player_count: "{player_count}"\n' if player_count else ""
        duration_yaml = f'  duration: "{duration}"\n' if duration else ""

        # Build design goals summary
        design_goals = f"""1. Target: {target}
2. Meccaniche principali: {', '.join(mechanics)}
3. Complessita': {complexity}/5"""
        if player_count:
            design_goals += f"\n4. Giocatori: {player_count}"
        if duration:
            design_goals += f"\n{'5' if player_count else '4'}. Durata: {duration} minuti"

        template_content = f"""---
command: invent
version: "1.0"

metadata:
  name: "{project_name}"
  description: "Template generato dal wizard interattivo"
  author: "Wizard"

{custom_prompt_yaml}context:
  theme: "{theme}"
  target_audience: "{target}"
{inspiration_yaml}

parameters:
  mechanics:
{mechanics_yaml}
  complexity: {complexity}
{player_count_yaml}{duration_yaml}  format: markdown
  output_file: "{output_file}"

content:
  idea_summary: |
    {idea_summary}

{constraints_yaml}---

# Design Goals

{design_goals}
"""

        # Ensure directory exists
        os.makedirs(os.path.dirname(template_path), exist_ok=True)

        with open(template_path, "w", encoding="utf-8") as f:
            f.write(template_content)

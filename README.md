# Boardgames Are Made of Rules

A command-line tool that uses local LLMs (via Ollama) to analyze, explain, fix, and even invent board games starting from their rulebooks in PDF or text format.

The system provides five tasks: explaining rules to different audiences, extracting game properties with optional BoardGameGeek comparison, reviewing rulebooks for issues, generating new game designs, and recommending strategic moves.


## Requirements

- Python 3.9+
- Ollama installed and running locally (`http://localhost:11434`)
- Rulebook files in PDF or TXT format


## Ollama Models Used

The project supports multiple models, each suited for different tasks. Pull them before running:

```bash
ollama pull llama3.2
ollama pull deepseek-r1:8b
ollama pull mistral-nemo:12b
ollama pull qwen2.5
ollama pull gemma3:4b
```

| Model | Alias | Best For |
|---|---|---|
| llama3.2:latest | llama | General tasks, explanations (default) |
| deepseek-r1:8b | deepseek | Reasoning, analysis, fix-rules |
| mistral-nemo:12b | mistral | Creative generation, invent |
| qwen2.5:latest | qwen | Structured analysis (32k context) |
| gemma3:4b | gemma | Lightweight explanations |


## Installation

```bash
git clone https://github.com/SydanJainen/BoardGameAreMadeOfRules
cd "Boardgames are made of rules"

pip install -r requirements.txt

ollama serve
```


## Usage Examples

Each example uses a rulebook from the `rulebooks/` folder.

### Explain

Explain a rulebook to a specific audience (child, adult, or expert):

```bash
python main.py explain --input rulebooks/wingspan.pdf --audience child --model llama
```

### Analyse

Extract game properties (mechanics, complexity, players, duration) and optionally compare with BoardGameGeek data:

```bash
python main.py analyse --input rulebooks/cascadia.pdf --bgg-name "Cascadia" --model qwen
```

### Fix-Rules

Identify ambiguities, missing rules, and logical inconsistencies in a rulebook:

```bash
python main.py fix-rules --input rulebooks/ticketToRide.pdf --model deepseek
```

### Invent

Generate a complete new board game design from a concept:

```bash
python main.py invent --concept "A cooperative game about exploring underwater caves" --model mistral
```

Or use the interactive wizard:

```bash
python main.py invent --wizard
```

### Recommend-Move

Recommend the best next move given the current game state:

```bash
python main.py recommend-move --rules rulebooks/Pandemic.pdf --state "2 players, 3 outbreaks occurred, blue disease cured, 4 cards in hand including Atlanta and Chicago" --model llama
```


## Common Options

All tasks accept these optional arguments:

| Flag | Description |
|---|---|
| `--model` | Model alias: llama, deepseek, mistral, qwen, gemma |
| `--output` | Save result to file (path) |
| `--format` | Output format: `markdown` (default) or `json` |
| `--pdf-mode` | PDF extraction method: `basic`, `plumber`, `ocr`, `tables`, `images` |


## Templates

Tasks can also be run from YAML template files:

```bash
python main.py --template templates/recommend-move/scenario_catan.yaml
```

Templates are available in the `templates/` folder for pre-configured scenarios.

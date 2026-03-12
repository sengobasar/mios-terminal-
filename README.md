# MIOS — AI Terminal Copilot

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-000000?logo=ai&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-v1.0%20Beta-orange)]()
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> A local-first, privacy-focused command-line assistant that understands errors, explains solutions, and executes fixes transparently.

---

## What MIOS Is

MIOS (Machine Intelligence Operating System) is an **AI-powered terminal copilot** that helps developers:

- **Debug errors** by analyzing stack traces and suggesting fixes
- **Translate natural language** to terminal commands
- **Diagnose system issues** (CPU, RAM, disk, processes)
- **Analyze logs** for errors and patterns
- **Explain commands** before execution
- **Remember context** across sessions

**Core Philosophy:** Diagnose → Explain → Plan → Execute (with confirmation)

**No black boxes.** Every action is transparent. Every command requires approval.

---

## Why MIOS Exists

### Problems Developers Face Daily

| Problem | MIOS Solution |
|---------|---------------|
| **Cryptic errors** (`ModuleNotFoundError`, `PermissionDenied`) | Parse error → explain cause → suggest fix |
| **Forgetting CLI syntax** (`tar`, `chmod`, `ssh`) | Natural language → terminal command |
| **Environment hell** (PATH issues, Python versions) | Automatic environment detection |
| **Build failures** (npm, pip, docker) | Read logs → propose fixes |
| **System slowness** (high CPU/RAM) | `mios doctor` → diagnose → suggest cleanup |

---

## Quick Start

### Installation

```bash
# Install MIOS (future PyPI release)
pip install mios

# Or install from source
git clone https://github.com/yourusername/mios.git
cd mios
pip install -e .
```

### Prerequisites

**Local LLM** (required for reasoning):
```bash
# Install Ollama
curl https://ollama.ai/install.sh | sh

# Pull a model
ollama pull phi
```

### Basic Usage

```bash
# Debug an error
mios debug

# System diagnostics
mios doctor

# Natural language commands
mios run

# Explain a command
mios explain "git rebase origin/main"

# Analyze logs
mios analyze server.log
```

---

## Core Capabilities (v1.0)

### 1. Error Debugging

```bash
$ mios debug

Paste your error:
ModuleNotFoundError: No module named 'numpy'

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Error Type: missing_package
Cause: numpy package not installed in current environment

Plan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Detect Python environment (venv/conda/system)
2. Install numpy using appropriate package manager
3. Verify installation

Suggested Fix
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

pip install numpy

Execute this plan? (y/n):
```

---

### 2. System Diagnostics

```bash
$ mios doctor

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
System Health Check
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CPU Usage:        35.2% ✓
RAM Usage:        62.1% ⚠
Disk Usage:       71.4% ⚠

Memory: 10.2 GB / 16.0 GB
Disk:   215 GB / 300 GB

Top Processes by CPU:
  chrome        12.3%
  python        8.7%
  vscode        5.2%

Recommendations:
  • Close unused browser tabs
  • Free up disk space (consider cleanup)
```

---

### 3. Natural Language Commands

```bash
$ mios run

> compress this folder

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Command Translation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Intent: compress_folder

Command:
  tar -czf archive.tar.gz folder/

Explanation:
  Creates compressed archive of folder/

Execute? (y/n):
```

**More examples:**
```
"find files larger than 1GB"  →  find . -size +1G
"list python files"           →  find . -name "*.py"
"kill process on port 8000"   →  kill $(lsof -ti:8000)
```

---

### 4. Command Explanation

```bash
$ mios explain "git rebase origin/main"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Command Explanation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Command: git rebase origin/main

What it does:
  Reapplies your local commits on top of the latest
  changes from origin/main branch.

⚠ Warning:
  This rewrites commit history. Do not rebase commits
  that have been pushed to shared branches.

When to use:
  • Before creating a pull request
  • To keep a clean linear history
  • When working on a feature branch

Alternative:
  git merge origin/main (preserves history)
```

---

### 5. Log Analysis

```bash
$ mios analyze server.log

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Log Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Errors:    2
Warnings:  5
Info:      127

Top Errors:
  DatabaseConnectionError  (line 45)
  TimeoutError             (line 103)

Patterns Detected:
  • Database connection timeouts (5x)
  • Memory warnings increasing over time

Recommendations:
  1. Check database connection pool settings
  2. Monitor memory usage trends
```

---

## Mathematical Framework

MIOS is fundamentally a **decision-making agent** that maps observations to actions through learned and rule-based policies.

### 1. Core Agent Model

```
a = π(U, S, C, T, E)
```

Where:
- `U` — User input (error, query, command)
- `S` — System state (CPU, RAM, processes)
- `C` — Context memory (previous commands, errors)
- `T` — Available tools (system_info, executor, analyzer)
- `E` — Past episodes (successful/failed attempts)
- `π` — Policy (LLM reasoning + rule-based logic)
- `a` — Action (command, explanation, plan)

---

### 2. Error Classification

Error parsing is a classification function:

```
f(e) → error_type
```

**Examples:**
```
ModuleNotFoundError    → missing_package
PermissionDenied       → permission_error
command not found      → missing_command
ImportError            → dependency_conflict
```

Implemented via **regex-based pattern matching** in `debug/error_parser.py`.

---

### 3. Intent Detection

Natural language understanding:

```
intent = g(U)
```

**Examples:**
```
"compress this folder"      → compress_folder
"find large files"          → find_large_files
"why is my pc slow"         → system_diagnosis
"explain git rebase"        → explain_command
```

Implemented in `ai/intent_classifier.py` using LLM-based classification.

---

### 4. Command Translation

Intent to executable command:

```
cmd = h(intent, U)
```

**Examples:**
```
compress_folder  → tar -czf archive.tar.gz folder/
find_large_files → find . -size +1G
system_diagnosis → psutil.cpu_percent(), psutil.virtual_memory()
```

Implemented in `core/interpreter.py`.

---

### 5. Planning Model

Agent generates a sequence of actions:

```
P = {a₁, a₂, ..., aₙ}
```

**Example plan for `ModuleNotFoundError`:**
```
P = {
  analyze_error,
  detect_environment,
  install_dependency,
  verify_installation
}
```

Each action `aᵢ` is executed sequentially with result evaluation after each step.

---

### 6. Tool Selection

Agent chooses the best tool for the task:

```
tool = argmax_{t ∈ T} score(t | U, S)
```

**Available tools:**
- `system_info` — CPU, RAM, disk diagnostics
- `log_analyzer` — Pattern detection in logs
- `environment_detector` — Python env detection (venv, conda)
- `executor` — Safe command execution
- `file_tools` — File search, analysis

Tool scoring considers:
- **Relevance** to user query
- **Safety** (read-only preferred)
- **Past success rate** (from episode memory)

---

### 7. Agent Loop (ReAct Model)

Closed-loop reasoning:

```
aₜ = π(U, S, C, Hₜ)
```

Where `Hₜ` is the history of previous actions and results.

**Agent cycle:**
```
observe  →  reason  →  act  →  evaluate  →  update memory
```

Implemented in `core/agent_loop.py` (v3 feature).

---

### 8. Task Graph Execution

Plans are represented as directed acyclic graphs:

```
G = (V, E)
```

Where:
- `V` — Tasks (nodes)
- `E` — Dependencies (edges)

**Example:**
```
install_dependency  →  retry_command
detect_environment  →  install_dependency
```

A task is **ready** if all dependencies are completed:

```
ready(v) = deps(v) ⊆ completed
```

---

### 9. Episode Memory

Each problem-solving session is stored as:

```
E = (U, P, R)
```

Where:
- `U` — Problem (error, query)
- `P` — Plan executed
- `R` — Result (success/failure)

**Policy improvement:**
```
πₙₑw = πₒₗ𝒹 + f(E)
```

Future versions will use episode memory for **reinforcement-like learning**.

---

## System Architecture

```
┌────────────────────────────────────────────────────────────┐
│                      User Input (CLI)                       │
└──────────────────────┬─────────────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────────┐
│           Intent Classifier (LLM + Rules)                 │
│  • debug_error                                            │
│  • system_diagnosis                                       │
│  • translate_command                                      │
│  • explain_command                                        │
└──────────────────────┬───────────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────────┐
│                   Agent Planner                           │
│  Generates multi-step plan: P = {a₁, a₂, ..., aₙ}        │
└──────────────────────┬───────────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────────┐
│                  Task Graph Scheduler                     │
│  Enforces dependency order                                │
└──────────────────────┬───────────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────────┐
│                   Tool Executor                           │
│  • system_info  • log_analyzer  • file_tools              │
│  • environment_detector  • command_executor               │
└──────────────────────┬───────────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────────┐
│                 Result Evaluator                          │
│  success? → update memory / retry? → next action         │
└──────────────────────┬───────────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────────┐
│              Context & Episode Memory                     │
│  • Context: last_error, last_fix, project_type           │
│  • Episodes: (problem, plan, result) tuples              │
└──────────────────────────────────────────────────────────┘
```

---

## Project Structure

```
mios/
│
├── cli/
│   └── main.py                  # Entry point (Typer CLI)
│
├── core/
│   ├── interpreter.py           # Natural language → command
│   ├── planner.py               # Multi-step plan generation
│   ├── executor.py              # Safe command execution
│   ├── agent_loop.py            # ReAct reasoning loop (v3)
│   ├── agent_planner.py         # LLM-based planning (v3)
│   ├── tool_registry.py         # Dynamic tool selection (v3)
│   ├── task_graph.py            # Dependency scheduler (v3)
│   └── result_evaluator.py      # Success detection (v3)
│
├── debug/
│   └── error_parser.py          # Regex-based error classification
│
├── tools/
│   ├── system_info.py           # CPU, RAM, disk diagnostics (psutil)
│   ├── log_analyzer.py          # Pattern detection in logs
│   ├── environment_detector.py  # Python env detection
│   ├── file_tools.py            # File search, analysis
│   └── process_tools.py         # Process management
│
├── ai/
│   ├── intent_classifier.py     # LLM-based intent detection
│   ├── llm_client.py            # Ollama API wrapper
│   └── prompt_templates.py      # System prompts for LLM
│
├── memory/
│   ├── context_store.py         # Session context (JSON)
│   └── episode_memory.py        # Past executions (SQLite) (v3)
│
├── config/
│   └── settings.py              # Configuration
│
├── utils/
│   └── helpers.py               # Utility functions
│
├── requirements.txt
└── README.md
```

---

## Dependencies

```txt
# Core
typer>=0.9.0
rich>=13.0.0
psutil>=5.9.0

# AI/LLM
ollama>=0.1.0

# Utilities
pydantic>=2.0.0
pathlib>=1.0.0
```

**Installation:**
```bash
pip install -r requirements.txt
```

---

## Development Roadmap

### ✅ Version 1.0 (Current) — Error Fixer

**Completed features:**
- CLI interface (`mios debug`, `mios doctor`)
- Error parsing and classification
- System diagnostics (CPU, RAM, disk)
- Natural language command translation
- Command explanation
- Log analysis
- Environment detection (venv, conda)
- Context memory

---

### 🚧 Version 2.0 (In Progress) — Terminal Copilot

**Goal:** Transform MIOS into a full terminal assistant.

**New features:**
- Enhanced intent classification
- Improved natural language understanding
- Command history integration
- Project-aware suggestions
- Interactive multi-turn conversations

---

### 📋 Version 3.0 (Planned) — Autonomous Agent

**Goal:** Multi-step autonomous problem-solving.

**New capabilities:**
- Agent loop with ReAct reasoning
- Task graph execution with dependencies
- Dynamic tool selection
- Result evaluation and retry logic
- Episode memory for learning

**Example workflow:**
```
User: "fix server.py"

Agent:
1. Run server.py → capture error
2. Analyze error → missing dependency
3. Detect environment → venv
4. Install dependency → pip install flask
5. Retry server.py → success
```

---

### 🔮 Version 4.0 (Future) — Project Intelligence

**Goal:** Understand entire codebases.

**Planned features:**
- Project scanner (AST parsing)
- Dependency analysis
- Code navigation
- Codebase search
- Safe file system operations
- Smarter LLM-based planning

---

### 🌟 Version 5.0 (Vision) — Devin-Style Agent

**Goal:** Fully autonomous coding agent.

**Capabilities:**
- Read entire projects
- Write and modify code
- Run tests automatically
- Fix bugs end-to-end
- Update dependencies
- Generate documentation

**Agent cycle:**
```
observe → reason → act → evaluate → learn
```

---

## Current Limitations

This is an honest prototype. Here are the constraints:

### 1. LLM Dependency
Requires local Ollama installation. **Resolution:** Ship with smaller embedded models in future.

### 2. Rule-Based Planning
Planner uses heuristics, not learned policies. **Resolution:** v3 introduces LLM-based planning.

### 3. No Multi-Turn Memory
Each command is independent. **Resolution:** v2 adds conversation history.

### 4. Limited Tool Set
Only basic system tools. **Resolution:** v4 adds file operations, code analysis.

### 5. No Learning
Cannot improve from mistakes yet. **Resolution:** v3 episode memory enables learning.

---

## Safety & Privacy

### Local-First Architecture
- **All processing runs locally** — no data sent to cloud
- LLM runs on your machine via Ollama
- No telemetry or usage tracking

### Command Confirmation
- **Every action requires approval** before execution
- Destructive commands are flagged with warnings
- Safety layer blocks dangerous patterns (`rm -rf /`)

### Transparent Actions
- **No black boxes** — every plan is shown before execution
- Step-by-step explanations
- Full command visibility

---

## Testing

Before using MIOS, run the test suite:

```bash
# Basic CLI test
mios --help

# Error debugging
echo "ModuleNotFoundError: numpy" | mios debug

# System diagnostics
mios doctor

# Natural language translation
echo "compress this folder" | mios run

# Command explanation
mios explain "git rebase origin/main"
```

---

## Contributing

MIOS is in active development. Contributions welcome!

**Priority areas:**
- Additional error patterns for `error_parser.py`
- New system tools in `tools/`
- Intent classification improvements
- LLM prompt engineering
- Testing and bug reports

---

## References

This project draws inspiration from:

1. **ReAct: Synergizing Reasoning and Acting in Language Models** (Yao et al., 2022) — Agent loop architecture
2. **Toolformer: Language Models Can Teach Themselves to Use Tools** (Schick et al., 2023) — Tool selection
3. **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (Wei et al., 2022) — Planning
4. **Devin: AI Software Engineer** — Vision for autonomous coding agent

---

## License

MIT License. See `LICENSE` for details.

---
**Project Goal:** Build a local, transparent, privacy-respecting AI assistant that makes terminal workflows faster and less frustrating for developers.

---

<div align="center">

**MIOS — Your local AI terminal copilot**

*Diagnose → Explain → Plan → Execute*

Made with 🤖 and ☕

</div>

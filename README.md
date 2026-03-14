<div align="center">

# 🤖 MIOS — AI Terminal Copilot

### *Local-First, Privacy-Focused Command-Line Intelligence*

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama)](https://ollama.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

![AI Powered](https://img.shields.io/badge/AI-Powered-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Research_Prototype-orange?style=for-the-badge)

**An experimental AI-powered terminal assistant that interprets natural language and executes developer commands.**

[🚀 Quick Start](#-quick-start) • [✨ What Works Now](#-what-works-now-v10) • [🏗️ Architecture](#-how-it-works) • [📖 Roadmap](#-development-roadmap)

</div>

---

## 💡 **What is MIOS?**

**MIOS (Machine Intelligence Operating System)** is an experimental AI terminal copilot that translates natural language into terminal commands. Think of it as a **local ChatGPT for your command line** — but everything runs on your machine with complete privacy.

### **Example Session:**

```bash
mios>: create hello.cpp and write hello world program
✓ File created: hello.cpp

mios>: open hello.cpp

--- hello.cpp ---
#include <iostream>
int main() {
    std::cout << "Hello World";
}

mios>: edit hello in hello.cpp and change it to hello world
✓ File modified: hello.cpp
```

---

## 🎯 **Why MIOS?**

| Developer Problem | MIOS Solution |
|-------------------|---------------|
| **Cryptic Errors** | Parse → Explain → Suggest fix |
| **Forgetting Syntax** | Natural language → Command |
| **Environment Issues** | Auto-detect → Diagnose |
| **Repetitive Tasks** | Natural language automation |

**Core Philosophy:**
```
Understand → Explain → Confirm → Execute
```

No black boxes. Every action shown. Every command requires approval.

---

## ✨ **What Works Now (v1.0)**

### ✅ **Currently Implemented:**

<table>
<tr>
<td width="50%">

#### 🔧 **File Operations**
- ✅ Create files with content
- ✅ Modify existing files
- ✅ Read file contents
- ✅ Natural language editing

</td>
<td width="50%">

#### 💻 **System Operations**
- ✅ Run shell commands
- ✅ Install Python packages
- ✅ System diagnostics (CPU, RAM, disk)
- ✅ Environment detection (venv/conda)

</td>
</tr>
<tr>
<td width="50%">

#### 🐛 **Debugging**
- ✅ Error parsing
- ✅ Error classification
- ✅ Fix suggestions
- ✅ Auto-retry with fixes

</td>
<td width="50%">

#### 🧠 **AI Features**
- ✅ Intent classification
- ✅ LLM command interpretation
- ✅ Context-aware responses
- ✅ Session memory

</td>
</tr>
</table>

---

## 🎯 **Core Capabilities**

### 1️⃣ **Natural Language Commands**

```bash
mios>: create test.txt and write hello world
✓ File created: test.txt

mios>: open test.txt
--- test.txt ---
hello world

mios>: install numpy
✓ Installing numpy...
✓ Successfully installed numpy-1.24.0
```

---

### 2️⃣ **Error Debugging**

```bash
$ python script.py
ModuleNotFoundError: No module named 'requests'

$ mios debug

📊 Error Analysis:
   Type: missing_package
   Package: requests

💡 Suggested Fix:
   pip install requests

Execute? (y/n): y
✓ Installed requests
✓ Ready to retry
```

**Supported Error Types:**
- `ModuleNotFoundError` → Auto-install
- `ImportError` → Dependency resolution
- `PermissionDenied` → Permission suggestions
- `SyntaxError` → Code correction hints

---

### 3️⃣ **System Diagnostics**

```bash
$ mios doctor

🏥 System Health Check

CPU:   35.2% ✓
RAM:   62.1% ⚠ (10.2 GB / 16.0 GB)
Disk:  71.4% ⚠ (215 GB / 300 GB)

🔥 Top Processes:
   chrome    12.3%
   python     8.7%
   vscode     5.2%

💡 Recommendations:
   • Consider closing unused tabs
   • Free up disk space
```

---

## 🏗️ **How It Works**

### **System Architecture:**

```
User Input (Natural Language)
         ↓
Intent Classifier
         ↓
    ┌────┴────┐
    ↓         ↓
Rule-Based   LLM
Interpreter  Fallback
    ↓         ↓
    └────┬────┘
         ↓
Action Parser (JSON)
         ↓
Tool Executor
         ↓
System Operation
         ↓
User Confirmation
```

### **The Agent Model:**

MIOS works as a decision-making agent:

```
action = policy(user_input, system_state, context)
```

The policy combines:
- **Rule-based logic** for common commands
- **LLM reasoning** for complex requests
- **Tool execution** for system operations

**Example Flow:**

```python
# User: "create hello.py"
intent = classify("create hello.py")  # → create_file
↓
if intent == "create_file":
    action = {"action": "create_file", "file": "hello.py"}
else:
    action = llm_interpret("create hello.py")
↓
execute(action)  # Creates the file
↓
confirm_with_user()  # Shows what was done
```

---

## ⚡ **Quick Start**

### 📦 **Installation**

```bash
# 1. Install Ollama (for local LLM)
curl https://ollama.ai/install.sh | sh

# 2. Pull a coding model
ollama pull deepseek-coder

# 3. Clone MIOS
git clone https://github.com/sengobasar/mios-terminal-.git
cd mios-terminal-

# 4. Install
pip install -e .
```

### ▶️ **Usage**

```bash
# Start interactive shell
mios

# Or use specific commands
mios debug        # Debug errors
mios doctor       # System check
```

---

## 📁 **Project Structure**

```
mios/
│
├── cli/
│   └── main.py              # CLI entry point
│
├── core/
│   ├── interpreter.py       # Command interpretation
│   ├── executor.py          # Tool execution
│   ├── session.py           # Session management
│   └── planner.py           # Multi-step planning (v2)
│
├── ai/
│   ├── intent_classifier.py # Intent detection
│   └── command_llm.py       # LLM integration
│
├── debug/
│   └── error_parser.py      # Error parsing
│
├── tools/
│   ├── system_info.py       # System diagnostics
│   └── file_tools.py        # File operations
│
└── requirements.txt
```

---

## 🚀 **Development Roadmap**

### ✅ **v1.0 — Current Release**

**What works:**
- ✅ File create/edit/read
- ✅ Command execution
- ✅ Package installation
- ✅ Error debugging
- ✅ System diagnostics
- ✅ Intent classification
- ✅ LLM fallback

---

### 🚧 **v2.0 — In Progress**

**Goal:** Better natural language understanding

**Planned:**
- 🔄 Command explanation (`mios explain "git rebase"`)
- 🔄 Log analysis (`mios analyze server.log`)
- 🔄 Multi-turn conversations
- 🔄 Command history awareness
- 🔄 Project context detection

---

### 📋 **v3.0 — Future**

**Goal:** Autonomous multi-step problem solving

**Vision:**
- 🔮 ReAct-style agent loop
- 🔮 Task graph execution
- 🔮 Automatic retry with learning
- 🔮 Episode memory (remember past fixes)
- 🔮 Multi-step planning

**Example workflow (not yet implemented):**

```
User: "fix server.py"

Agent:
1. Run server.py → capture error
2. Analyze → missing flask
3. Install → pip install flask
4. Retry → success
```

---

### 🔮 **v4.0+ — Long-term Vision**

**Goal:** Project-wide intelligence

**Ideas:**
- 🌟 Code navigation
- 🌟 Project scanning
- 🌟 Dependency analysis
- 🌟 Test generation
- 🌟 Documentation generation

---

## 🎯 **Technical Details**

### **Intent Classification**

Common patterns are detected via rules:
- `"create {file}"` → `create_file`
- `"install {package}"` → `install_package`
- `"run {command}"` → `run_command`

Unknown patterns fall back to LLM interpretation.

### **LLM Integration**

LLM generates structured JSON:

```json
{
  "action": "create_file",
  "file": "hello.py",
  "content": "print('hello')"
}
```

Allowed actions:
- `create_file`
- `modify_file`
- `read_file`
- `run_command`
- `install_package`

### **Error Parsing**

Regex-based classification:
- `ModuleNotFoundError: (.+)` → Extract package name
- `PermissionError` → Detect permission issues
- `SyntaxError` → Code syntax problems

---

## 🔒 **Safety & Privacy**

### **100% Local**
- ✅ All processing on your machine
- ✅ No cloud API calls (except local Ollama)
- ✅ No telemetry
- ✅ No data collection

### **User Confirmation**
- ✅ Every command requires approval
- ✅ Dangerous operations flagged
- ✅ Full transparency on actions

---

## ⚠️ **Current Limitations**

**Honest assessment:**

1. **LLM Required** — Needs Ollama installed locally
2. **Limited Tools** — Only basic file/system operations (v1)
3. **No Multi-Turn Memory** — Each command is independent
4. **Rule-Based Planning** — Not yet fully autonomous
5. **No Learning** — Doesn't improve from past mistakes (yet)

**These are being addressed in v2 and v3.**

---

## 📦 **Dependencies**

```bash
typer>=0.9.0      # CLI framework
rich>=13.0.0      # Terminal formatting
psutil>=5.9.0     # System info
ollama>=0.1.0     # Local LLM
```

Install all:
```bash
pip install -r requirements.txt
```

---

## 🎓 **Use Cases**

| Scenario | How MIOS Helps |
|----------|----------------|
| 🎓 **Learning CLI** | Natural language → commands |
| 🐛 **Debugging** | Auto-parse errors → suggest fixes |
| 💼 **DevOps Tasks** | Automate repetitive operations |
| 🔬 **Research** | Quick system diagnostics |

---

## 🤝 **Contributing**

This is an active research prototype. Contributions welcome!

**Priority areas:**
- 🔧 New tools (file operations, git commands)
- 🎯 Better intent patterns
- 🐛 Error pattern improvements
- 📝 Documentation
- 🧪 Testing

---

## 📚 **Inspiration**

This project draws ideas from:
- **ReAct** (Yao et al., 2022) — Agent reasoning patterns
- **Toolformer** (Schick et al., 2023) — LLM tool use
- **SWE-agent** — Autonomous debugging
- **Devin** — Long-term vision for coding agents

---

## 📄 **License**

MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

### ⭐ **Star if you find this interesting!**

[![GitHub stars](https://img.shields.io/github/stars/sengobasar/mios-terminal-?style=social)](https://github.com/sengobasar/mios-terminal-)

**Made with 🤖 and ☕**

---

**MIOS — Your Local AI Terminal Copilot**

*Understand → Explain → Confirm → Execute*

</div>

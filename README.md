# MiniPy Compiler - Basic Edition

A compiler for a Python-like language called **MiniPy**, built for hackathons and compiler learning!

🚀 This project tokenizes, parses, and compiles MiniPy code into **bytecode**, and executes it with a custom **stack-based virtual machine** — all through a clean **Streamlit UI**.

---

## 🌟 Features

- [x] Lexer using **PLY (Python Lex-Yacc)**
- [x] Parser using **PLY Yacc**
- [x] Custom AST (Abstract Syntax Tree)
- [x] Bytecode Generator (STACK-based)
- [x] Basic Virtual Machine (VM)
- [x] Streamlit UI for web interaction
- [x] Clean separation of code: `lexer.py`, `parser.py`, `codegen.py`, `interpreter.py`
- [x] 📦 Streamlit-ready and deployable!

---

## 📁 Project Structure

```bash
minipy-compiler-basic/
├── app.py                  # Streamlit frontend
├── lexer.py                # Tokenizer
├── parser.py               # Grammar & AST generation
├── codegen.py              # Bytecode generation
├── interpreter.py          # Stack-based virtual machine
├── minipy_ast.py           # Custom AST node classes (Assign, Print, If, etc.)
├── examples/test.minipy    # Example MiniPy source code
├── requirements.txt        # Required Python libraries
└── README.md               # You're here!
```

## 🧪 Sample MiniPy Code

```python
x = 5
y = 10
if x < y
    print(x + y)
else
    print(x - y)
```

---

## 🧾 Bytecode Output

```text
PUSH 5
STORE x
PUSH 10
STORE y
LOAD x
LOAD y
<
JZ else
LOAD x
LOAD y
+
PRINT
JMP end
else:
LOAD x
LOAD y
-
PRINT
end:
```

---

## 🖥️ Local Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/rishi02102017/minipy-compiler-basic.git
cd minipy-compiler-basic
```

---

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the compiler locally

```bash
streamlit run app.py
```

---

## 🌐 Deploy to Streamlit Cloud

You can make your compiler available **24x7 online** via Streamlit Cloud:

1. Push this code to a public GitHub repo
2. Visit 👉 [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **“New app”**
4. Select your repo: `rishi02102017/minipy-compiler-basic`
5. Set:
   - 🗂️ **Main file**: `app.py`
   - 🛠️ **Python version**: `3.10` or above
6. Click **Deploy** 🚀

💡 Now you can share the live link with anyone — no need to keep your PC running!

---

##  Tech Stack

- **Python 3.10+**
- **PLY** – Lex/Yacc for Python
- **Streamlit** – UI framework
- **GitHub** – for version control & deployment

---

## 📚 Concepts You’ll Learn

- Lexical Analysis (tokenization)
- Context-Free Grammar
- Abstract Syntax Trees (AST)
- Stack-based Code Generation
- Writing a Virtual Machine
- UI + Backend integration (via Streamlit)

---

## ## **Contributors**
- Jyotishman Das: Lead Developer and Project Contributor.
 **[Rishi02102017](https://github.com/rishi02102017)**  

---


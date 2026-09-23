# Codveda Python Development Internship

A collection of Python projects and exercises completed during a Python development internship. This repository showcases hands-on learning in Python fundamentals, user interface development with Gradio, interactive notebook exercises, and practical problem-solving tasks across basic, intermediate, and advanced levels.

## Overview

This repository is designed to demonstrate progression in Python development skills through a structured set of tasks. It includes:

- simple console and GUI-based calculator logic
- a task management application
- notebook-based learning exercises
- an advanced file encryption/decryption utility
- interactive applications built with Gradio

The projects are beginner-friendly, easy to run locally, and suitable for learning Python app development and UI-based workflows.

## Project Structure

```text
Codveda_Python-Dev-Intern/
├── files/
|     ├── docs.txt
|     └── docs_encrypt_file.txt
├── Level1-Basic_Task1.py
├── Level1-Basic_Task2.ipynb
├── Level1-Basic_Task3.ipynb
├── Level2-Intermediate_Task1.py
├── Level2-Intermediate_Task2.ipynb
├── Level2-Intermediate_Task3.ipynb
├── Level3-Advanced_Task2.py
├── Level3-Advanced_Task3.py
├── LICENSE
└── README.md
```

### File Highlights

- `Level1-Basic_Task1.py` — a basic calculator with addition, subtraction, multiplication, and division using Gradio.
- `Level2-Intermediate_Task1.py` — a to-do list application with add, complete, and delete features.
- `Level3-Advanced_Task2.py` — a Caesar cipher-based file encryption/decryption tool.
- `*.ipynb` files — notebook-based tasks covering interactive Python exercises and experimentation.

## Key Features

- Interactive Python apps using Gradio
- Real-time task tracking with status updates
- Calculator operations with input validation and error handling
- File encryption and decryption using a Caesar cipher
- Easy-to-understand code for learning and experimentation
- Notebook-based tasks for exploratory development
- Clean Python logic organized by skill level

## Technologies Used

- Python 3
- Gradio
- Jupyter Notebook
- Git and GitHub
- VS Code / Python development environment
- Standard Python libraries such as `string`

## Prerequisites

Before running the code in this repository, make sure you have the following installed:

- Python 3.9 or later
- `pip` (Python package installer)
- Jupyter Notebook (for `.ipynb` files)
- A modern code editor such as VS Code

## Installation Guide

Follow the steps below to set up the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/MoshoodSO/Codveda_Python-Dev-Intern.git
cd Codveda_Python-Dev-Intern
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it depending on your operating system:

- Windows:

```bash
venv\Scripts\activate
```

- macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install gradio jupyter ipykernel
```

### 4. Run a project

Example: run the calculator application:

```bash
python Level1-Basic_Task1.py
```

This starts a local Gradio app in the browser, typically at:

```text
http://127.0.0.1:7860/
```

To run the to-do list app:

```bash
python Level2-Intermediate_Task1.py
```

To work with notebook files:

```bash
jupyter notebook
```

## Example Usage

### Calculator example

```python
from Level1-Basic_Task1 import Calculator

calc = Calculator()
print(calc.addition(10, 5))
print(calc.multiplication(4, 3))
```

### Task management example

```python
# The Gradio app allows users to:
# - add a task
# - mark it as completed
# - delete it from the list
```

### Encryption example

```python
# The Caesar cipher encrypts each letter by shifting it within the alphabet.
# Example: A -> D with a shift of 3
```

## How the Projects Work

### 1. Basic Calculator
The calculator app accepts two numbers and an operation, then performs the selected arithmetic operation. It includes error handling to prevent division by zero.

### 2. To-Do List
The to-do application uses a class-based structure to track tasks in two categories:

- Undone
- Done

Users can add, complete, and delete tasks from the UI.

### 3. File Encryption/Decryption
The advanced task uses a Caesar cipher to shift characters in uppercase letters. It reads a text file, encrypts or decrypts its contents, and saves the result as a new file.

## Run Notes

- Some Gradio apps launch a local web interface automatically.
- For sharing outside your local machine, use `share=True` in `launch()` if needed.
- Notebook files can be opened and executed interactively in Jupyter.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome. If you would like to improve the project, feel free to fork the repository, make changes, and submit a pull request.

## Contact

For questions or collaboration opportunities, please reach out through the repository owner on GitHub:

- GitHub: [MoshoodSO](https://github.com/MoshoodSO)

---

This repository is a practical learning portfolio that demonstrates growth in Python development and user-facing application building.

# ai agent

A small AI agent that runs on your laptop. It can use a calculator.

## Setup 

1. Install Ollama: https://ollama.com/download and open it
2. Install Python: https://www.python.org/downloads/ (on Windows, check "Add python.exe to PATH" in the installer)


## If it doesn't work

- "Open the Ollama app first": Ollama isn't running.
- "command not found": Python didn't install right. Reinstall it and reopen Terminal or IDE

## How it works

When you ask a question, the AI decides if it needs the calculator. If it does, the code runs the calculator and gives the AI the answer, then the AI replies to you. That loop is what makes it an agent, essentially. The whole thing is about 50 lines in agent.py.
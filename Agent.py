# all built into python, no installs
import json, urllib.request, urllib.error

# the ai brain (about 1 GB)
MODEL = "qwen2.5:1.5b"

# the tool: a normal function the ai can use
def calculator(expression):
    try:
        return str(eval(expression, {"__builtins__": {}}))
    except Exception as e:
        return f"Error: {e}"

# describe the tool so the ai knows it exists
tools = [{"type": "function", "function": {
    "name": "calculator",
    "description": "Do math",
    "parameters": {"type": "object", "properties": {"expression": {"type": "string"}}},
}}]

# send something to ollama and get its reply
def ollama(path, data):
    return json.load(urllib.request.urlopen("http://localhost:11434/api/" + path, json.dumps(data).encode()))

# make sure ollama is open and the brain is downloaded
try:
    ollama("show", {"model": MODEL})
except urllib.error.HTTPError:
    print("Downloading the AI (about 1 GB). Hang tight...")
    ollama("pull", {"model": MODEL, "stream": False})
except urllib.error.URLError:
    exit("Open the Ollama app first, then try again.")

print("Ready!
chat = []

# chat forever
while True:
    chat.append({"role": "user", "content": input("you > ")})
    reply = ollama("chat", {"model": MODEL, "messages": chat, "tools": tools, "stream": False})["message"]

    # the agent part: if the ai wants the calculator, run it and ask again
    while reply.get("tool_calls"):
        chat.append(reply)
        for call in reply["tool_calls"]:
            result = calculator(**call["function"]["arguments"])
            print("  (used calculator:", result + ")")
            chat.append({"role": "tool", "content": result})
        reply = ollama("chat", {"model": MODEL, "messages": chat, "tools": tools, "stream": False})["message"]

    chat.append(reply)
    print("agent >", reply["content"], "\n")
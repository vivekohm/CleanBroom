import subprocess

def ask_llama(prompt):
    result = subprocess.run(
        ["ollama", "run", "gemma3"], #gemma3
        input=prompt,
        text=True,
        capture_output=True,
        encoding="utf-8"
    )
    return result.stdout
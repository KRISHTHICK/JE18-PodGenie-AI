import subprocess

def generate_script(text, style="Conversational"):
    prompt = f"Convert this blog/news content into a {style} podcast script:\n\n{text[:1000]}"
    result = subprocess.run(["ollama", "run", "tinyllama", prompt], capture_output=True, text=True)
    return result.stdout.strip()

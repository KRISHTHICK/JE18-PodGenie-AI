import subprocess

def simulate_conversation(text):
    intro = "Host: Welcome to today's show. We’re diving into a hot topic!"
    prompt = f"Create a 2-person podcast discussion based on:\n\n{text[:1000]}"
    result = subprocess.run(["ollama", "run", "tinyllama", prompt], capture_output=True, text=True)
    conversation = result.stdout.strip()
    return f"{intro}\n\n{conversation}"


import requests
import time
import json

BASE = "http://localhost:11434"
MODEL = "campus-helper"


def normal_response(prompt):
    print("\n--- NORMAL RESPONSE ---")
    start = time.perf_counter()

    response = requests.post(
        f"{BASE}/api/generate",
        json={"model": MODEL, "prompt": prompt, "stream": False},
        timeout=180
    )
    response.raise_for_status()
    data = response.json()

    elapsed = time.perf_counter() - start
    print(data.get("response", ""))
    print("Total time:", round(elapsed, 2), "seconds")

    count = data.get("eval_count", 0)
    duration = data.get("eval_duration", 0) / 1_000_000_000
    if duration > 0:
        print("Tokens per second:", round(count / duration, 2))


def streaming_response(prompt):
    print("\n--- STREAMING RESPONSE ---")
    start = time.perf_counter()
    first_token_time = None
    token_count = 0

    with requests.post(
        f"{BASE}/api/generate",
        json={"model": MODEL, "prompt": prompt, "stream": True},
        stream=True,
        timeout=180
    ) as response:
        response.raise_for_status()

        for line in response.iter_lines():
            if not line:
                continue

            data = json.loads(line)
            chunk = data.get("response", "")

            if chunk:
                if first_token_time is None:
                    first_token_time = time.perf_counter()
                print(chunk, end="", flush=True)

            if data.get("done"):
                token_count = data.get("eval_count", 0)

    end = time.perf_counter()
    print()

    if first_token_time is not None:
        print("TTFT:", round(first_token_time - start, 3), "seconds")

    print("Total time:", round(end - start, 2), "seconds")
    print("Tokens per second:", round(token_count / (end - start), 2))


def openai_compatible(prompt):
    print("\n--- OPENAI-COMPATIBLE ENDPOINT ---")

    response = requests.post(
        f"{BASE}/v1/chat/completions",
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a pirate. Answer in pirate style."
                },
                {"role": "user", "content": prompt}
            ],
            "stream": False
        },
        timeout=180
    )
    response.raise_for_status()
    data = response.json()
    print(data["choices"][0]["message"]["content"])


if __name__ == "__main__":
    normal_response("Explain an API key with one simple example.")
    streaming_response("What is a prompt? Explain simply.")
    openai_compatible("Explain what a computer stack is.")

import openai
from pathlib import Path

MODEL = 'gpt-4'
openai.api_key = "API-Key-Here"

def ask_question(messages):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        stream=True  # Set stream=True for streaming completions
    )
    output = ""
    for chunk in response:
        if "delta" in chunk["choices"][0]:
            delta = chunk["choices"][0]["delta"]
            if "content" in delta:
                content = delta["content"]
                output += content
                print(content, end="")  # Add end parameter to prevent newline character

    return output

if __name__ == "__main__":
    message = "createe me one paragraph of a realistic story from the news"
    message = [{"role": "system", "content":"You are a helpful assistant."},
               {"role": "user", "content": message},]
    for i in range(10):
        print()
    ask_question(message)
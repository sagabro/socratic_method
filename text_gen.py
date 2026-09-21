from openai import OpenAI

# Point to the local LM Studio server
# (Ensure the port matches the one shown in your LM Studio Local Server tab)
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


def generate_text(prompt: str, system_prompt: str = "You are a helpful assistant.") -> str:
    try:
        completion = client.chat.completions.create(
            # LM Studio automatically uses the currently loaded model on your server,
            # so you can pass any string name here or your exact model identifier.
            model="local-model",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,  # Controls creativity (0.0 is deterministic, 1.0 is creative)
            max_tokens=500  # Limits the maximum response length
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}\n(Make sure LM Studio is running and the local server is started!)"


# Example Usage
if __name__ == "__main__":
    user_prompt = "Write a short poem about a programmer fixing a bug at 2 AM."
    print("Sending prompt to LM Studio...")

    response = generate_text(prompt=user_prompt)

    print("\n--- Generated Text ---")
    print(response)

import os
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="lm-studio")

def chat_session():
    system_prompt = "You will teach me how to do something using the Socratic method."
    messages = [
        {"role": "system", "content": system_prompt}
    ]

    print("Chatbot initialized with LM Studio! Type 'quit' or 'exit' to stop.\n")

    while True:
        try:
            user_input = input("You: ")
            
            if user_input.strip().lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
                
            if not user_input.strip():
                continue

            messages.append({"role": "user", "content": user_input})

            completion = client.chat.completions.create(
                model="gemma-4-12b-it-qat",
                messages=messages,
                temperature=0.2,
                max_tokens=500
            )
            
            bot_reply = completion.choices[0].message.content
            print(f"\nBot: {bot_reply}\n")
            
            messages.append({"role": "assistant", "content": bot_reply})

        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("(Make sure LM Studio is running, the local server is started, and 'gemma-4-12b-it-qat' is loaded!)\n")
            break

if __name__ == "__main__":
    chat_session()

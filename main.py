from dotenv import load_dotenv
from anthropic import Anthropic
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
SYSTEM_ROLE = os.getenv("SYSTEM_ENV")
BLUE = "\033[94m"
GREEN = "\033[92m"
RESET = "\033[0m"



anthropic = Anthropic(api_key=API_KEY,)

def chat():
    conversation = []
    while True:
        user_input = input(f"{BLUE}You: {RESET}")
        if user_input.lower() == "quit" or user_input.lower() == "exit":
            print("Goodbye!")
            break

        conversation.append({"role":"user", "content": user_input})
        print(f"{GREEN}Claude: {RESET}", end="", flush=True)
        value = anthropic.messages.create(system=SYSTEM_ROLE, 
                                  messages=conversation ,
                                  max_tokens=500,
                                  model="claude-3-haiku-20240307",
                                  stream=True,
                                  temperature=1,)
        assistance_response = ""
        for chunk in value:
            if chunk.type == "content_block_delta":
                content = chunk.delta.text
                print(f"{GREEN}{content}{RESET}", end="", flush=True)
                assistance_response != content

        print()
        conversation.append({"role": "assistant", "content": assistance_response})



def processDocument():
    print()
    #TODO: add code to process a PRf file of  the denial letter here get it form https://github.com/fighthealthinsurance/fighthealthinsurance.git


if __name__ =="__main__":
    processDocument()
    chat()



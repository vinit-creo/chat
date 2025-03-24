from dotenv import load_dotenv
from anthropic import Anthropic
from claims import denial_letter, insurance_policy
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

       
    print(f"{GREEN}Claude: {RESET}", end="", flush=True)
    value = anthropic.messages.create(system=SYSTEM_ROLE, 
                         messages=[
            {"role": "user", "content": f"Generate summary of the points with which I can appeal to the denial letter by an health insurance company as text here {denial_letter} as per the policy document {insurance_policy}. Do not assume anything, use the facts that are as present in the two inputs. Basically generate a few bullet points to include in my appeal letter, along with that based on the two inputs here do let me know the probability of my appeals claims to be reconsidered."}
        ],
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



def processDocument():
     # TODO: add code to process a PRf file of  the denial letter here get it form https://github.com/fighthealthinsurance/fighthealthinsurance.git
    print()



if __name__ =="__main__":
    chat()



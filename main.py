from dotenv import load_dotenv
from anthropic import Anthropic
from claims import denial_letter
import json
from results.results import format
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
SYSTEM_ENV = """You are an analyst and your job is to find the reason for the denial of insurance in that letter. You have a hight aptitude for reasoning and  document perusal."""
GREEN = "\033[92m"
RESET = "\033[0m"

anthropic = Anthropic(api_key=API_KEY,)


def chat():
    json_format =  get_data()
    print(f"json_format ", json_format)
    
    value = anthropic.messages.create(system=SYSTEM_ENV, 
                         messages=[
            {"role": "user", "content": f"Analyze the data here {denial_letter} and get references of the reasons for denial of in the letter and for specific language that has been used in the letter to specify the cause for denial. Give it to me in json  as this {json_format} format. Populate the fields accordingly. Your response should be just in json format nothing else."}
        ],
                                  max_tokens=1000,
                                  model="claude-3-haiku-20240307",
                                  stream=False,
                                  temperature=0,
            )
    print(f"{GREEN}{value.content[0].text}{RESET}", end="", flush=True)
   
   


def get_data():
    data = json.dumps(format)
    return data

if __name__ =="__main__":
    chat()




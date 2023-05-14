import openai
import os
import re
import sys
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
from colored import fg, attr
from dotenv import load_dotenv

load_dotenv()
# Load your API key from an environment variable or secret management service
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

def chat(question=None):
    print(f"{fg('blue')}ChatGPT Terminal Version{attr(0)}")
    print("Enter 'quit' to exit the program\n")
    if question:
        message = question
    else:
        message = input(f"{fg('green')}You: {attr(0)}")
        print()
    while message != 'quit':
        try:
            response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo", 
              messages=[
                  {
                    "role": "system",
                    "content": "You are a helpful assistant."
                  },
                  {
                    "role": "user",
                    "content": message
                  }
              ]
            )
            if response['choices'] and response['choices'][0]['message']:
                answer = response['choices'][0]['message']['content']
                # If the answer contains Python code
                if '```' in answer:
                    # Use a regex to find all code blocks
                    code_blocks = re.findall(r'```(.*?)```', answer, re.DOTALL)
                    for block in code_blocks:
                        # Highlight the Python code
                        highlighted_code = highlight(block, PythonLexer(), TerminalFormatter())
                        # Replace the Python code in the answer with the highlighted Python code
                        answer = answer.replace('```'+block+'```', highlighted_code)
                print(f"{fg('blue')}ChatGPT: {attr(0)}", answer + "\n")
            else:
                print(f"{fg('blue')}ChatGPT: {attr(0)} Sorry, I didn't understand that.\n")
            if question:
                break
            else:
                message = input(f"{fg('green')}You: {attr(0)}")
                print()
        except Exception as e:
            print("An error occurred: ", str(e))

def main():
    question = None
    if len(sys.argv) > 1:
        question = sys.argv[1]
    chat(question)

if __name__ == "__main__":
    main()

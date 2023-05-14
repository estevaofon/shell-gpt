# Shell-GPT

Shell-GPT is a terminal-based chatbot using OpenAI's powerful GPT-3.5-turbo model. This project allows you to interact with the model directly from your terminal. It also includes syntax highlighting for Python code in the chat responses.

## Features

- Interactive chat with GPT-3.5-turbo from your terminal.
- Python code syntax highlighting for improved readability.
- Ability to pass a question as a command line argument.

## Requirements

- Python 3.7 or later
- OpenAI Python package
- Pygments package for Python code highlighting
- Colored package for colored terminal text
- Dotenv package for environment variable management

## Setup

1. Clone the repository: `git clone https://github.com/yourusername/shell-gpt.git`
2. Navigate to the project directory: `cd shell-gpt`
3. Install the requirements: `pip install -r requirements.txt`
4. Set up your OpenAI API key in a `.env` file in the project root directory. The key should be assigned to the `OPENAI_API_KEY` variable. For example:

    ```plaintext
    OPENAI_API_KEY=yourapikey
    ```

## Usage

To start a chat, simply run:

```bash
python shell_gpt.py
```

## Contribution
Contributions, issues, and feature requests are welcome!

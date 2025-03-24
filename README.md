# Increasingly Verbose App

A fun application that takes a sentence and generates increasingly verbose versions of it using GPT. Built with Streamlit and OpenAI's API.

## Prerequisites

- Python 3.11+
- OpenAI API key

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/increasingly_verbose_app.git

# Navigate to the project directory
cd increasingly_verbose_app

# Install dependencies
pip install -r requirements.txt

# Set up your OpenAI API key
# Create a .streamlit/secrets.toml file with:
# [openai]
# API_KEY = "your-api-key-here"
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default web browser. Simply:
1. Enter your text in the input area
2. Click 'Get Response'
3. Watch as it transforms your text into a more verbose version

## Examples

Original: "The cat sat."
Result: "The domesticated mammal of the species Felis catus assumed a position wherein its posterior was placed upon a surface."

## Acknowledgements

- Built with Streamlit and OpenAI's GPT API
- Inspired by "r/IncreasinglyVerbose" subreddit - https://www.reddit.com/r/IncreasinglyVerbose/

## License

This project is licensed under the MIT License - see the LICENSE file for details.

# Domo (Arigato), an AI Thank You Card App

Author: Ian Mosley Email: ianamo86@gmail.com License: MIT

Domo will help you write your thank you cards. Create a CSV file with fields for Recipient, Gift, and Email, and Domo will read in the data and use the LLM of your choice to create a file with prewritten thank you emails. (Gemma2:2b seems to work well.) Requires a working Ollama installation as well as the Ollama and Pandas packages.

## How to Use

First install dependencies, particularly [Ollama](https://ollama.com). Then clone the repo and proceed as follows (Linux/Mac):

```
pip install ollama pandas
ollama pull gemma2:2b
```

Or the LLM of your choice. Edit `thankyou.csv` with the relevant information, then:

`python domo.py`

You will find the emails in `thankyouemails.md`. 

## Other Questions

*Does using this make me a bad person?*

Perhaps. But if you've got a huge list to work through and it saves your sanity, who's to say, really?
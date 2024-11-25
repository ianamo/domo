import ollama
import pandas as pd

filename = 'thankyou.csv'
output_file = 'thankyouemails.md'
GEN_AGENT ='gemma2:2b'
emails_text = []

thankyouinfo = pd.read_csv(filename)

for i, row in thankyouinfo.iterrows():
    prompt = f"You are writing a thoughtful thank you email to {row['Recipient']}. They gave us a {row['Gift']}. Address the email to {row['Email']}. Be specific about how we will enjoy this gift."
    r = ollama.generate(model=GEN_AGENT, prompt=prompt)
    emails_text.append(r.response)

with open(output_file,'w') as f:
    f.write("\n".join(emails_text))
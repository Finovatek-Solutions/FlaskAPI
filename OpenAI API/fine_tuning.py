from openai import OpenAI
import pandas as pd

df = pd.read_csv(r"C:\Users\aj824\OneDrive - University of Puerto Rico\Classes\INSO4151 (Capstone)\FlaskAPI\OpenAI API\banco popular personal - banco popular personal.csv", delimiter=",")

descriptions = df["Description"].to_list()
results = []
#print(descriptions)

client = OpenAI(api_key = "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")

for description in descriptions:
    completion = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:finovatek-solutions:capstone:8zp7M20L",
        messages=[
            {"role": "system", "content": "You are an assistant that classify transactions into categories based on description"},
            {"role": "user", "content": "Classify this transaction decsription: " + description}
        ]
        )
    print(completion.choices[0].message)
    results.append(completion.choices[0].message.content)
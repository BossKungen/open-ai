import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = OPENAI_API_KEY

chat = True
while chat:
    chat = str(input('Enter your text: '))
    if chat == 'q': 
        chat = False
    else:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chat,
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
        )
        print("Answer: " + response["choices"][0]["text"])
print("The End!")


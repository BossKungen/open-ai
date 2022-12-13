import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = OPENAI_API_KEY

def chat_response(chat: str):
    return  openai.Completion.create(
        model="text-davinci-003",
        prompt=chat,
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
        )

def spell_correction(chat: str):
    return openai.Edit.create(
        model="text-davinci-edit-001",
        input=chat,
        instruction="Fix the spelling mistakes"        
        )

play = True
while play:
    nbr = int(input("Pick type\n1 - Answer a quation\n2 - Answer a question with sarcasm\n3 - Spell correction\nDitt val: "))
    chat = str(input('Enter your text: '))
    if chat == 'q': 
        play = False
    else:
        match nbr:
            case 1:
                response = chat_response(chat)
                print("Answer: " + response["choices"][0]["text"])
            case 2:
                chat = "Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\n" + chat
                response = chat_response(chat)
                print("Answer: " + response["choices"][0]["text"])
            case 3:
                response = spell_correction(chat)
                print("Answer: " + response["choices"][0]["text"])
                
print("The End!")


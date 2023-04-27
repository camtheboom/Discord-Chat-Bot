import random
import openai
# BOT_URL = 'https://discord.com/api/oauth2/authorize?client_id=1098637017014882495&permissions=1099511629824&scope=bot'

openai.api_key = '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'
model_engine = "text-davinci-003"

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if p_message.split(" ")[0] == "!roll":
        gameList = []
        for i in p_message.split(" ")[1:]:
            gameList.append(i)
    
        return str(random.choice(gameList))

    if p_message[0] == "!" and p_message.split(" ")[0] != "!roll" and p_message.split(" ")[0] != "!help":
        #Generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=p_message[1:],
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        return str(response)

    if p_message == '!help':
        return '`Welcome to Camerons chat bot. Here are some commands you can use: \n\n- !roll <game1> <game2> <game3> ... <gameN> (This gives you a random game that you listed) \n\n- !help (For list of commands)\n\n- !<text> (Prompt the chatgpt bot by putting an ! mark in front of the text)`'
        
    return


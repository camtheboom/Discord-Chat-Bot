import discord
import responses

async def send_message(message, user_message):
    try:
        response = responses.get_response(user_message)
        await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA5ODYzNzAxNzAxNDg4MjQ5NQ.GkCD0V.AQ7OGCaHL_0KJf5xBtbRveRgKOel5A4u5A38mI'

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    # client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{client.user} Has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        await send_message(message, user_message)

    client.run(TOKEN)
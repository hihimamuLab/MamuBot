import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Ready as {self.user}!')
        print(discord.__version__)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('token name')

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Ready as {self.user}!')
        print(discord.__version__)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTA2OTc4OTE3NjU5MTA0MDU5Mg.GSiDbp.MHK-gYfwQKUfPaApsOoi0-yraKW2FAH0RTxtUg')

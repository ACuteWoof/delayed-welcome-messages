import discord
import os
import asyncio

intents = discord.Intents.default()
intents.members = True

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_member_join(self, member):
        await asyncio.sleep(int(os.getenv("DELAY_IN_SECONDS")))
        channel =  discord.utils.get(member.guild.channels, name=os.getenv("CHANNEL_TO_WELCOME"))
        print(member)
        await channel.send(f'Welcome {member.mention} to the community!')

client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_BOT_TOKEN"))

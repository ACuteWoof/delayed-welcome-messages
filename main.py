import discord
import os
import asyncio
import requests
import json
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bin_key = os.getenv("BIN_KEY")

def get_bin() :
    url = "https://api.jsonbin.io/v3/b/61a20e4701558c731cc9a7ff/latest"
    headers = {
      'X-Master-Key': bin_key
    }

    req = requests.get(url, json=None, headers=headers)
    print(req.text)
    return json.loads(req.text)

def add_server(sid) :
    url = 'https://api.jsonbin.io/v3/b/61a20e4701558c731cc9a7ff'
    headers = {
      'Content-Type': 'application/json',
      'X-Master-Key': bin_key
    }
    data = getbin()["record"][sid] = {"channel":"general","delay_in_seconds":"10","welcome_format":"Welcome {0.mention}!"}
    req = requests.put(url, json=data, headers=headers)
    print(req.text)

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    intents=discord.Intents.all(),
)

class AdminOnly(commands.Cog, description="Admin commands"):
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def update_delay(self, ctx, delay):
        url = 'https://api.jsonbin.io/v3/b/61a20e4701558c731cc9a7ff'
        headers = {
          'Content-Type': 'application/json',
          'X-Master-Key': bin_key
        }
        try:
            data = get_bin()["record"]
            data[str(ctx.guild.id)]["delay_in_seconds"] = delay
        except:
            add_server(str(ctx.guild.id))
            data = get_bin()["record"]
            data[str(ctx.guild.id)]["delay_in_seconds"] = delay
        finally:
            req = requests.put(url, json=data, headers=headers)
            print(req.text)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def update_format(self, ctx, fmt):
        url = 'https://api.jsonbin.io/v3/b/61a20e4701558c731cc9a7ff'
        headers = {
          'Content-Type': 'application/json',
          'X-Master-Key': bin_key
        }
        try:
            data = get_bin()["record"]
            data[str(ctx.guild.id)]["welcome_format"] = fmt
        except:
            add_server(str(ctx.guild.id))
            data = get_bin()["record"]
            data[str(ctx.guild.id)]["welcome_format"] = fmt
        finally: 
            req = requests.put(url, json=data, headers=headers)
            print(req.text)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def update_channel(self, ctx, channel):
        url = 'https://api.jsonbin.io/v3/b/61a20e4701558c731cc9a7ff'
        headers = {
          'Content-Type': 'application/json',
          'X-Master-Key': bin_key
        }
        try:
            data = get_bin()["record"]
            data[str(ctx.guild.id)]["channel"] = channel
        except:
            add_server(str(ctx.guild.id))
            data = get_bin()["record"]
            data[str(ctx.guild.id)]["channel"] = channel
        finally:
            req = requests.put(url, json=data, headers=headers)
            print(req.text)


@bot.event
async def on_ready():
    print(f'Logged on!')

@bot.event
async def on_member_join(member):
    try:
        delay = get_bin()["record"][str(member.guild.id)]["delay_in_seconds"]
    except:
        add_server(str(member.guild.id))
    finally:
        fmt = get_bin()["record"][str(member.guild.id)]["welcome_format"]
        welcome_channel = get_bin()["record"][str(member.guild.id)]["channel"]
        await asyncio.sleep(int(delay))
        if member in member.guild.members:
            channel = discord.utils.get(member.guild.channels, name=welcome_channel)
            print(member)
            await channel.send(fmt.format(member))
        else:
            print("Left before welcomed.")

bot.add_cog(AdminOnly())
bot.run(os.getenv("DISCORD_BOT_TOKEN"))

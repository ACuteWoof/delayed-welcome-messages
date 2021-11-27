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
    with open("settings.json", "r") as file:
        data = json.load(file)
    print(data)
    return data

def add_server(sid) :
    data = get_bin()
    data["record"][sid] = {"channel":"general","delay_in_seconds":"10","welcome_format":"Welcome {0.mention}!"}
    json.dump(data, fp=open("settings.json", "w"))

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    intents=discord.Intents.all(),
)

class AdminOnly(commands.Cog, description="Admin commands"):
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def update_delay(self, ctx, delay):
        try:
            data = get_bin()
            data["record"][str(ctx.guild.id)]["delay_in_seconds"] = delay
        except KeyError:
            add_server(str(ctx.guild.id))
            data = get_bin()
            data["record"][str(ctx.guild.id)]["delay_in_seconds"] = delay
        finally:
            json.dump(
                    data,
                    fp=open(
                         "settings.json", "w"
                        )
                    )

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def update_format(self, ctx, fmt):
        try:
            data = get_bin()
            data["record"][str(ctx.guild.id)]["welcome_format"] = fmt
        except KeyError:
            add_server(str(ctx.guild.id))
            data = get_bin()
            data["record"][str(ctx.guild.id)]["welcome_format"] = fmt
        finally:
            json.dump(
                    data,
                    fp=open(
                         "settings.json", "w"
                        )
                    )

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def update_channel(self, ctx, channel):
        try:
            data = get_bin()
            data["record"][str(ctx.guild.id)]["channel"] = channel
        except KeyError:
            add_server(str(ctx.guild.id))
            data = get_bin()
            data["record"][str(ctx.guild.id)]["channel"] = channel
        finally:
            json.dump(
                    data,
                    fp=open(
                         "settings.json", "w"
                        )
                    )


@bot.event
async def on_ready():
    print(f'Logged on!')

@bot.event
async def on_member_join(member):
    try:
        delay = get_bin()["record"][str(member.guild.id)]["delay_in_seconds"]
    except KeyError:
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

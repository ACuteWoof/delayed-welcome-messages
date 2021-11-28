# Delayed Welcomer Bot

![Made With Love](http://ForTheBadge.com/images/badges/built-with-love.svg)

![License](https://img.shields.io/github/license/acutewoof/delayed-welcome-messages?color=%23b5bd68&style=for-the-badge)

This bot allows you to set custom welcome messages within a delay of a member joining a server.
It's #FOSS and meant to be copied so feel free to copy the code and use it in your own bot.

## Running the bot

- Clone this repository `git clone https://github.com/acutewoof/delayed-welcome-messages.git`
- Set the environment variable `DISCORD_BOT_TOKEN` to your bot's token
- Run `main.py` using python

## Commands

Command prefix: `!`

There are only a few commands provided with the Cog present in [main.py](https://github.com/ACuteWoof/delayed-welcome-messages/blob/main/main.py). Those commands are used to customise server-specific settings for the welcomer.

- `update_channel` - Update/change the channel that the bot should send the welcome message in.
- `update_delay` - Update/change the delay (in seconds) for the bot to wait before sending the welcome message.
- `update_format` - Update/change the format of the welcome message. Use `{0.mention}` to mention the user, `{0.name}` to show the username, or just `{0}` to show their username. Example valid format: "Hello {0.mention}! Welcome to the community of the Woofs! Hope you have a good time here!"

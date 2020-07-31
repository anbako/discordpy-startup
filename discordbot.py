from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.category_id == 630802817522728960:
        await message.channel.edit(position=0)

bot.run(token)

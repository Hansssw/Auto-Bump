import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive
import os

prefix = "$$"

keep_alive()
token = os.getenv("token")



bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)



@bot.command()
async def helpbump(ctx):
    await ctx.message.delete()
    await ctx.send('**$$Autobump: !d bump. $$StopAutoBump: Stops the bot. This code can bypass ban**')

@bot.command()
async def stopautobump(ctx):
    await ctx.message.delete()
    await ctx.send('**AutoBump is now Disabled 😺 (not currently working, delete channel to make it stop.) $$Autobump to enable it again!**')
    global dmcs
    dmcs = False


@bot.command(pass_context=True)
async def autobump(ctx):
    await ctx.message.delete()
    await ctx.send('**AutoBump is now Enabled 😺! Thank you for using this script**')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(3)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            print(f"{Fore.GREEN}Break for an hour")
            await asyncio.sleep(7200)


            

            
keep_alive()
bot.run(os.getenv('token'), bot=False)

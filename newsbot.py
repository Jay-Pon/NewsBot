import discord
from discord.ext import commands, tasks
from itertools import cycle


status = cycle(['Destroying', 'rebuilding'])

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    change_status.start()
    print('Bot is online')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))



client.run('ODAwNzQ2NzM3ODg2ODIyNDMw.YAWngw.fp95gR95AEKStzvpcrQnNxEE5zo')
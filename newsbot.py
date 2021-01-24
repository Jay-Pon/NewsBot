import discord
from discord.ext import commands, tasks
from itertools import cycle
from politics import politics_get_news
from science import science_daily_get_news
from tech import tech_get_news
from entertainment import entertainment_get_news

status = cycle(['Destroying', 'rebuilding'])

client = commands.Bot(command_prefix = '/')

#NEWS CONSTANTS
POL_NEWS = 1
ENT_NEWS = 1
SCI_NEWS = 1
TECH_NEWS = 1

#NEWS CHANNELS
client.SCIENCE_CHANNEL = None
client.POLI_CHANNEL = None
client.TECH_CHANNEL = None
client.ENT_CHANNEL = None

@client.event
async def on_ready():
    change_status.start()
    print('Bot is online')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def news(ctx, genre, keyword, number = 5):
    #set genres will be 'science', 'tech', 'politics', 'entertainment'
    if genre == 'tech':
        tech_news = tech_get_news(number)
        ctx.send(tech_news)

    elif genre == 'science':
        mi, mh, msh, st, si, sh = science_daily_get_news(1)

        embed = discord.Embed(
            title = mh,
            colour = discord.Colour.blue()
        )

        embed.add_field(name = "_" * 256, value = msh, inline=False)
        embed.set_image(url = mi)

        await client.SCIENCE_CHANNEL.send(embed = embed)

    elif genre == 'politics':
        poli_news = politics_get_news(keyword, number)
        ctx.send(poli_news)

    elif genre == 'entertainment':
        entertainment_news = entertainment_get_news(number)
        ctx.send(entertainment_news)
    else:
        await ctx.send("Enter an appropriate category!")

@tasks.loop(hours = 24)
async def daily_science():
    mi, mh, msh, st, si, sh = science_daily_get_news(1)

    embed = discord.Embed(
        title = mh,
        colour = discord.Colour.blue()
    )

    embed.add_field(name = 'subheadline', value = msh, inline=False)
    embed.set_image(url = mi)

    await client.science_channel.send(embed = embed)

@tasks.loop(hours = 24)
async def daily_tech():
    pass

@tasks.loop(hours = 24)
async def daily_ent():
    pass

@client.command()
async def setup(ctx):
    client.SCIENCE_CHANNEL = discord.utils.get(ctx.guild.channels, name='science')
    print("IN THE SETUP", client.SCIENCE_CHANNEL)
    client.poli_channel = discord.utils.get(ctx.guild.channels, name='political')
    client.tech_channel = discord.utils.get(ctx.guild.channels, name='technology')
    client.ent_channel = discord.utils.get(ctx.guild.channels, name='entertainment')
    await client.SCIENCE_CHANNEL.send("SUCCESSFULLY FOUND SCIENCE")
    await client.POLI_CHANNEL.send("SUCCESSFULLY FOUND POLITICAL")
    await client.TECH_CHANNEL.send("SUCCESSFULLY FOUND TECHNOLOGY")
    await client.ENT_CHANNEL.send("SUCCESSFULLY FOUND ENTERTAINMENT")

#make set up command

client.run('ODAwNzQ2NzM3ODg2ODIyNDMw.YAWngw.wV6Q3oQnmVGU8X2j9qlc16Jau-o')
import discord
from discord.ext import commands, tasks
from itertools import cycle
from politics import daily_politics_news
from science import science_daily_get_news
from tech import daily_tech_news
from entertainment import daily_entertainment_news

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
        t, l, i, img = daily_tech_news(1)

        embed = discord.Embed(
            title = t[0],
            colour = discord.Colour.blue()
        )

        embed.add_field(name = "_" * 256, value = i[0], inline=False)
        embed.set_image(url = img)

        await client.TECH_CHANNEL.send(embed = embed)

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
        h, i, l, img = daily_politics_news()

        embed = discord.Embed(
            title = h,
            colour = discord.Colour.blue()
        )

        embed.add_field(name = "_" * 256, value = i, inline=False)
        embed.set_image(url = img)

        await client.POLI_CHANNEL.send(embed = embed)

    elif genre == 'entertainment':
        h, l, i = daily_entertainment_news(1)

        embed = discord.Embed(
            title = h[0],
            colour = discord.Colour.blue()
        )

        embed.add_field(name = "_" * 256, value = l[0], inline=False)
        embed.set_image(url = i[0])

        await client.ENT_CHANNEL.send(embed = embed)
    else:
        await ctx.send("Enter an appropriate category!")

@tasks.loop(hours = 24)
async def daily_science():
    mi, mh, msh, st, si, sh = science_daily_get_news(1)

    embed = discord.Embed(
        title = mh,
        colour = discord.Colour.blue()
    )

    embed.add_field(name = "_" * 256, value = msh, inline=False)
    embed.set_image(url = mi)

    await client.SCIENCE_CHANNEL.send(embed = embed)

@tasks.loop(hours = 24)
async def daily_tech():
    t, l, i, img = daily_tech_news(1)

    embed = discord.Embed(
        title = t[0],
        colour = discord.Colour.blue()
    )

    embed.add_field(name = "_" * 256, value = i[0], inline=False)
    embed.set_image(url = img)

    await client.TECH_CHANNEL.send(embed = embed)

@tasks.loop(hours = 24)
async def daily_ent():
    h, l, i = daily_entertainment_news(1)

    embed = discord.Embed(
        title = h[0],
        colour = discord.Colour.blue()
    )

    embed.add_field(name = "_" * 256, value = l[0], inline=False)
    embed.set_image(url = i[0])

    await client.ENT_CHANNEL.send(embed = embed)  

@tasks.loop(hours = 24)
async def daily_poli():
    h, i, l, img = daily_politics_news()

    embed = discord.Embed(
        title = h,
        colour = discord.Colour.blue()
    )

    embed.add_field(name = "_" * 256, value = i, inline=False)
    embed.set_image(url = img)

    await client.POLI_CHANNEL.send(embed = embed)

@client.command()
async def setup(ctx):
    client.SCIENCE_CHANNEL = discord.utils.get(ctx.guild.channels, name='science')
    print("IN THE SETUP", client.SCIENCE_CHANNEL)
    client.POLI_CHANNEL = discord.utils.get(ctx.guild.channels, name='political')
    client.TECH_CHANNEL = discord.utils.get(ctx.guild.channels, name='technology')
    client.ENT_CHANNEL = discord.utils.get(ctx.guild.channels, name='entertainment')
    await client.SCIENCE_CHANNEL.send("SUCCESSFULLY FOUND SCIENCE")
    await client.POLI_CHANNEL.send("SUCCESSFULLY FOUND POLITICAL")
    await client.TECH_CHANNEL.send("SUCCESSFULLY FOUND TECHNOLOGY")
    await client.ENT_CHANNEL.send("SUCCESSFULLY FOUND ENTERTAINMENT")

#make set up command

client.run('ODAwNzQ2NzM3ODg2ODIyNDMw.YAWngw.Vo53iCVE-44RwtFCahzpteph_Z8')





















@client.command()
async def daily_test(ctx, genre, keyword, number = 5):
    #set genres will be 'science', 'tech', 'politics', 'entertainment'
    if genre == 'tech':
        t, l, i, img = daily_tech_news(1)

        embed = discord.Embed(
            title = t[0],
            colour = discord.Colour.blue()
        )

        embed.add_field(name = "_" * 256, value = i[0], inline=False)
        embed.set_image(url = img)

        await client.TECH_CHANNEL.send(embed = embed)

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
        h, i, l, img = daily_politics_news()

        embed = discord.Embed(
            title = h,
            colour = discord.Colour.blue()
        )

        embed.add_field(name = "_" * 256, value = i, inline=False)
        embed.set_image(url = img)

        await client.POLI_CHANNEL.send(embed = embed)

    elif genre == 'entertainment':
        h, l, i = daily_entertainment_news(1)

        embed = discord.Embed(
            title = h[0],
            colour = discord.Colour.blue()
        )

        embed.add_field(name = "_" * 256, value = l[0], inline=False)
        embed.set_image(url = i[0])

        await client.ENT_CHANNEL.send(embed = embed)
    else:
        await ctx.send("Enter an appropriate category!")
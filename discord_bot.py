import random
import asyncio
import aiohttp
import json
import discord
from discord import Game
from discord.ext.commands import Bot

TOKEN = 'XXXX'

BOT_PREFIX = ("!")
client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'Strong no.',
        'Maybe not.',
        'Not entirely sure.',
        'Most likely.',
        'Yeah. 100% yeah.',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name=" with my homework"))
    print("Logged in as " + client.user.name)

@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Current bitcoin price is: $" + response['bpi']['USD']['rate'])

@client.command()
async def lastfm():
    url = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=sh4dowjoez&api_key=b72ae44e3bf067b7ae00a4c6f0eabbd2&limit=1&format=json'
    async with aiohttp.ClientSession() as session:  
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Joe is currently listening to: " + response['recenttracks']['track']['url'])

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

client.run(TOKEN)











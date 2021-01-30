import os
import random
from discord.ext import commands
from dotenv import load_dotenv

import discord
from dotenv import load_dotenv
import stock

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
os.system('python stock.py')
bot = commands.Bot(command_prefix='!')


client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    #print(f'Company Code of the desired Company')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    quotes = [
        'Hello, Hope you bought Pizza!',
        'Hello, Glad you are here!',
    ]
    if "$code " in message.content:
       quote = message.content
       codeparts = quote.split()
       code = codeparts[1]
       stock.company = code
       os.system('python stock.py')
    elif "hi " in message.content.lower():
        response = random.choice(quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException
    elif message.content =='update':
        await message.channel.send(file=discord.File('C:/Users/hp/Desktop/Project/Stock.csv'))
        await message.channel.send(file=discord.File('C:/Users/hp/Desktop/Project/images/fig1.png'))
        await message.channel.send(file=discord.File('C:/Users/hp/Desktop/Project/images/fig2.png'))
        #await message.channel.send(file=discord.File('C:/Users/hp/Desktop/Project/images/fig3.png'))
        #await message.channel.send("Hi!")
    elif "Stockupdatesbot.logout()" == message.content.lower():
        await client.close()

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

    

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


client.run(TOKEN)
bot.run(TOKEN)
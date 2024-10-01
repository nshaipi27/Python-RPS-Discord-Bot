import discord
from discord.ext import commands
import random 

intents = discord.Intents.all()
client = discord.Client(intents = intents)
bot = commands.Bot(command_prefix='!', intents = intents)

@bot.command()
async def rps(ctx, user_choice: str):
    rps_choices = ['rock', 'paper', 'scissors']
    if user_choice not in rps_choices:
        await ctx.send('Invalid choice. Please choose rock, paper, or scissors')
        return
    bot_choice = random.choice(rps_choices)
    result = winner(user_choice, bot_choice)
    
    await ctx.send(f'I chose {bot_choice}. {result}')

@bot.command(name = 'sock')
async def sock(ctx):
    await ctx.send('Please make sure to also type rock, paper, or scissors when calling the !rps command')
       

def winner (user, bot):
    if user == bot:
        return "It's a tie!"
    elif (user == 'rock' and bot == 'scissors') or (user == 'paper' and bot == 'rock') or (user == 'scissors' and bot == 'paper'):
        return "You win!"
    else:
        return "You lose!"

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('YOUR_BOT_TOKEN')
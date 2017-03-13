import discord
from discord.ext import commands
import random
import logging

description = '''A test bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
logging.basicConfig()

bot = commands.Bot(command_prefix='?', description=description)
client = discord.Client()
games = ('Destiny','Rainbow 6 Siege','OverWatch','Path of Exile','TF2','GTA5','CS:GO','Metal Gear Solid V','Terraria','Minecraft','Rocket League')
answer = ('Most definitely','Definetely No','My sources say yes','My sources say no','NO - It may cause disease contraction',"Don't count on it",'Maybe','For sure','Totally','Nope','Ask me again later','Go search it up on Google' )

@bot.event
async def on_ready():
    print('Logged in as')
    print('TesBot')
    print(282997301042085889)
    print('------')

@bot.command()
async def changeGame(playing : str):
	await bot.change_presence(game=discord.Game(name='{}'.format(playing)))
	await bot.say ('Game Changed.')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

"""	
@bot.command()
async def repeat(times : int, content='repeating...'):
    """ """Repeats a message multiple times.""" """
    for i in range(times):
        await bot.say(content)
"""
@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='TesBot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')
	
@cool.command(name='Neville')
async def neville():
    """Is the bot cool?"""
    await bot.say('Yes, Neville is cool.')

@cool.command(name='Bogusstarwarsguy')
async def bogus():
    """Is the bot cool?"""
    await bot.say('Yes, Bogusstarwarsguy is cool.')	
	
@bot.command(description='For when you wanna know what game to play')
async def rgame():
    """Chooses random game."""
    await bot.say(random.choice(games))

@bot.command(description='combine two names to make a cute nickname for a couple.')
async def ship(name1 : str, name2 : str):
	nname1 = (len(name1) / 2)
	nname2 = (len(name2) / 2)
	newname1 = name1[:len(name1)//2]
	newname2 = name2[len(name2)//2:]
	shipname = newname1 + newname2
	await bot.say('Your shipped name is {}.'.format(shipname))
	
@bot.command(description='Answers any yes/no question. Use quotes around the question.')
async def eightball(*question : str):
	"""Answers any yes/no question. Use quotes around the question."""
	await bot.say('**Your question is:** {}'.format(question))
	await bot.say('**The answer is:** {}'.format(random.choice(answer)))

bot.run('MjgyOTk3MzAxMDQyMDg1ODg5.C6KbeQ.QMzhuYjGQy2BGcrXMz248qajUQ4')
import discord
from discord.ext import commands
import random
import asyncio
import logging
import youtube_dl
import aiohttp
import websockets

description = '''A test bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
logging.basicConfig()

"""discord.AppInfo(owner(id=199972785714364421))"""
bot = commands.Bot(command_prefix='?', description=description)
client = discord.Client()
games = ('Destiny','Rainbow 6 Siege','OverWatch','Path of Exile','TF2','GTA5','CS:GO','Metal Gear Solid V','Terraria','Minecraft','Rocket League')
answer = ('Most definitely','Definetely No','My sources say yes','My sources say no','NO - It may cause disease contraction',"Don't count on it",'Maybe','For sure','Totally','Nope','Ask me again later','Go search it up on Google' )
ownerid=('199972785714364421')

'''if not discord.opus.is_loaded():
	discord.opus.load_opus()'''

async def timepurgey(time: int, channel: object):
    await bot.wait_until_ready()
    counter = 0
    while not bot.is_closed:
        counter += 1
        await bot.send_message(channel,counter)
        deleted = await bot.purge_from(channel)
        await asyncio.sleep(time)  # task runs every "time" seconds

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
	if message.content.startswith ('?setGame'):
		print (message.author.id)
		if ownerid == message.author.id:
			playin = message.content.split('?setGame ', 1)[1]
			await bot.change_presence(game=discord.Game(name='{}'.format(playin[1])))
			await bot.send_message (message.channel, 'Game Changed.')	
		else:
			await bot.send_message(message.channel, 'Get the owner to change it.')
	await bot.process_commands(message)
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

	
'''@bot.command()
async def repeat(times : int, content='repeating...'):
    Repeats a message multiple times.
    for i in range(times):
        await bot.say(content)
'''
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
async def eightball(*, question : str):
	"""Answers any yes/no question. Use quotes around the question."""
	await bot.say('**Your question is:** {}'.format(question))
	await bot.say('**The answer is:** {}'.format(random.choice(answer)))

@bot.command(pass_context = True)
async def purge(ctx):
    if ownerid == ctx.message.author.id:
        deleted = await bot.purge_from(ctx.message.channel)
        await bot.say('Deleted {} message(s)'.format(len(deleted)))
    else:
        await bot.say('Get the owner to Commence the purge.')

@bot.command(pass_context=True)
async def timepurge(ctx, *, time: int):
    if ownerid == ctx.message.author.id:
        channel = ctx.message.channel
        bot.task = bot.loop.create_task(timepurgey(time, channel))
    else:
        await bot.say('Get the owner to Commence the purge.')

@bot.command(pass_context=True)
async def stoppurge (ctx):
    if ownerid == ctx.message.author.id:
        bot.task.cancel()
        await bot.say("Purge Stopped.")
    else:
        await bot.say('Get the owner to Stop the purge.')

@bot.command(pass_context = True)
async def disconnect(ctx):
    for x in bot.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()

@bot.command(pass_context = True)
async def wow(ctx, *, song : str ):
	voice = await bot.join_voice_channel(ctx.message.author.voice_channel)
	if song.startswith('d'):
		player = voice.create_ffmpeg_player('Darude-Dankstorm.mp3')
	else:
		player = voice.create_ffmpeg_player('SHOTS FIRED.mp3')
	player.start()
	

bot.run('MjgyOTk3MzAxMDQyMDg1ODg5.C6KbeQ.QMzhuYjGQy2BGcrXMz248qajUQ4')
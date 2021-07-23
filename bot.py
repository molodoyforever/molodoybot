import random
from sys import prefix
import discord
from discord import activity
from discord import channel
from discord.channel import VoiceChannel
from discord.ext import commands
from discord.message import Message
from discord.utils import get

client = commands.Bot( command_prefix = "+")
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence( status = discord.Status.idle, activity = discord.Game("Жизнь"))

#привки
hello_world = [ "hi", "Hello", "Привет", "Хелоу", "ку", "Здарова", "Здравствуй"]
answer_words = [ "узнать о сервере", "что тут делать?", "команды", "чем тут занятся?" ]
poka = [ "спокойной ночи", "сладких снов", "до завтра", "до встречи", "я спать", "иду спать" ]

@client.command( pass_context = True)

async def say (ctx, *, arg):
    author = ctx.message.author
    await ctx.channel.purge(limit = 1)
    await ctx.send ( arg )
 
@client.event

#ответы на фразы 
async def on_message( message ):
    await client.process_commands( message )
    msg = message.content.lower()
    if msg in hello_world:
        await message.channel.send("Привет, чего хотел?")
    
    if msg in answer_words:
        await message.channel.send("Пропиши команду !!help для подробной информации.")
    
    if msg in poka:
        await message.channel.send("Надеюсь, увидимся ещё!")

#удалим сообщения
@client.command( pass_context = True)
@commands.has_permissions( administrator = True )

async def clear(ctx, amount = 20):
    await ctx.channel.purge( limit = amount )

#kick
@client.command( pass_context = True)
@commands.has_permissions( administrator = True )

async def kick(ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge(limit = 1)

    await member.kick(reason = reason)
    await ctx.send( f"User { member.mention } kicked" )

#ban
@client.command( pass_context = True)
@commands.has_permissions( administrator = True )

async def ban(ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge(limit = 1)

    await member.ban(reason = reason)
    await ctx.send( f"User { member.mention } banned" )
#unban
@client.command( pass_context = True)
@commands.has_permissions( administrator = True )

async def unban( ctx, *, member ):
    await ctx.channel.purge(limit = 1)

    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        member = ban_entry.user

        await ctx.guild.unban( member )
        await ctx.send( f"User { member.mention } unbanned" )

        return

#help
@client.command( pass_context = True)
async def help( ctx ):
    emb = discord.Embed(title = "Навигация по командам")

    emb.add_field(name = "+help", value = "Это сообщение" )
    emb.add_field(name = "+say", value = "Фраза от имени бота" )
    emb.add_field(name = "+clear", value = "Очистка чата" )
    emb.add_field(name = "+обнять", value = "RP:Обнять участника сервера" )
    emb.add_field(name = "+поцеловать", value = "RP:Поцеловать участника сервера" )
    emb.add_field(name = "+убить", value = "RP:Убить участника сервера" )
    emb.add_field(name = "+лизнуть", value = "RP:Лизнуть участника сервера" )
    emb.add_field(name = "+курить", value = "RP:Покурить" )
    emb.add_field(name = "+join", value = "Пригласить бота в голосовой канал" )
    emb.add_field(name = "+leave", value = "Выгнать бота с голосового канала" )
    emb.add_field(name = "+mute/+unmute", value = "Ограничить участника в правах на сервере" )
    emb.add_field(name = "+kick", value = "Выгнать участника сервера" )
    emb.add_field(name = "+ban", value = "Забанить участника" )
    emb.add_field(name = "+unban", value = "Вернуть доступ к серверу" )
    
    await ctx.send( embed = emb )

#mute
@client.command()
@commands.has_permissions( administrator = True )

async def mute(ctx, member: discord.Member ):
    await ctx.channel.purge(limit = 1)

    mute_role = discord.utils.get(ctx.message.guild.roles, name = "MUTE")

    await member.add_roles(mute_role)

#unmute
@client.command()
@commands.has_permissions(administrator=True)

async def unmute(ctx, member:discord.Member):
    await ctx.channel.purge(limit=1)

    mute_role = discord.utils.get(ctx.message.guild.roles, name='MUTE')

    await member.remove_roles(mute_role)

#присоединение 
@client.command()

async def join( ctx ):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)
    
    if voice and voice.is_connected():
        await voice.move_to(channel)
    
    else:
        voice = await channel.connect()

#отсоединиться 

@client.command()

async def leave( ctx ):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)
    
    if voice and voice.is_connected():
        await voice.disconnect()
    
    else:
        voice = await channel.connect()

#обнять 
@client.command()

async def обнять( ctx, user: discord.User, *, Notes):
    await ctx.channel.purge(limit = 1)
    hugGifs = ["https://media.giphy.com/media/svXXBgduBsJ1u/giphy.gif",
    "https://media.giphy.com/media/qscdhWs5o3yb6/giphy.gif",
    "https://media.giphy.com/media/du8yT5dStTeMg/giphy.gif",
    "https://media.giphy.com/media/u9BxQbM5bxvwY/giphy.gif"]
    embed = discord.Embed(description = f"{ctx.message.author.mention} обнял(а) {user.mention}, {Notes}")
    embed.set_image(url=random.choice(hugGifs))

    await ctx.send(embed=embed)

#поцеловать
@client.command()

async def поцеловать( ctx, user: discord.User, *, Notes):
    await ctx.channel.purge(limit = 1)
    kissGifs = ["https://media.giphy.com/media/G3va31oEEnIkM/giphy.gif",
    "https://media.giphy.com/media/G3va31oEEnIkM/giphy.gif",
    "https://media.giphy.com/media/bGm9FuBCGg4SY/giphy.gif",
    "https://media.giphy.com/media/nyGFcsP0kAobm/giphy.gif",
    "https://media.giphy.com/media/zkppEMFvRX5FC/giphy.gif",
    "https://media.giphy.com/media/FqBTvSNjNzeZG/giphy.gif",
    "https://media.giphy.com/media/dP8ONh1mN8YWQ/giphy.gif",
    "https://i.gifer.com/2lte.gif"]
    embed = discord.Embed(description = f"{ctx.message.author.mention} поцеловал(а) {user.mention}, {Notes}")
    embed.set_image(url=random.choice(kissGifs))

    await ctx.send(embed=embed)

#убить
@client.command()

async def убить( ctx, user: discord.User, *, Notes):
    await ctx.channel.purge(limit = 1)
    killGifs = ["https://media.giphy.com/media/11HeubLHnQJSAU/giphy.gif",
    "https://media.giphy.com/media/eLsxkwF5BRtlK/giphy.gif",
    "https://media.giphy.com/media/3F9duvK4t9hzW/giphy.gif",
    "https://media.giphy.com/media/yy1rPT45jdX1K/giphy.gif",
    "https://media.giphy.com/media/XRr6w71DZxXig/giphy.gif",
    "https://media.giphy.com/media/oQtO6wKK2q0c8/giphy.gif",
    "https://i.gifer.com/1SgY.gif",
    "https://i.gifer.com/TS0a.gif",
    "https://i.gifer.com/OWOO.gif"]
    embed = discord.Embed(description = f"{ctx.message.author.mention} убил(а) {user.mention}, {Notes}")
    embed.set_image(url=random.choice(killGifs))

    await ctx.send(embed=embed)

#лизнуть
@client.command()

async def лизнуть( ctx, user: discord.User, *, Notes):
    await ctx.channel.purge(limit = 1)
    lickGifs = ["https://i.gifer.com/8ZwP.gif",
    "https://i.gifer.com/8Zwm.gif",
    "https://i.gifer.com/1UUs.gif",
    "https://i.gifer.com/TiOB.gif",
    "https://i.gifer.com/7BW.gif"]
    embed = discord.Embed(description = f"{ctx.message.author.mention} лизнул(а) {user.mention}, {Notes}")
    embed.set_image(url=random.choice(lickGifs))

    await ctx.send(embed=embed)

#курить
@client.command()

async def курить( ctx, *, Notes):
    await ctx.channel.purge(limit = 1)
    smokeGifs = ["https://i.gifer.com/NPV4.gif",
    "https://i.gifer.com/Mv.gif",
    "https://i.gifer.com/Vzt4.gif",
    "https://i.gifer.com/CY0.gif",
    "https://i.gifer.com/14n1.gif",
    "https://i.gifer.com/8YuB.gif",
    "https://i.gifer.com/74G.gif",
    "https://i.gifer.com/2qvr.gif",
    "https://i.gifer.com/1fTa.gif"]
    embed = discord.Embed(description = f"{ctx.message.author.mention} покурил, {Notes}")
    embed.set_image(url=random.choice(smokeGifs))

    await ctx.send(embed=embed)


token = open( "token.txt", "r" ).readline()

client.run( token )



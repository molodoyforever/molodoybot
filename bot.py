from os import name
from sys import prefix
import discord
from discord import activity
from discord import channel
from discord.channel import VoiceChannel
from discord.ext import commands
from discord.message import Message
from discord.utils import get

client = commands.Bot( command_prefix = "!!")
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

    emb.add_field(name = "!!help", value = "Это сообщение" )
    emb.add_field(name = "!!say", value = "Фраза от имени бота" )
    emb.add_field(name = "!!clear", value = "Очистка чата" )
    emb.add_field(name = "!!join", value = "Пригласить бота в голосовой канал" )
    emb.add_field(name = "!!leave", value = "Выгнать бота с голосового канала" )
    emb.add_field(name = "!!mute/!!unmute", value = "Ограничить участника в правах на сервере" )
    emb.add_field(name = "!!kick", value = "Выгнать участника сервера" )
    emb.add_field(name = "!!ban", value = "Забанить участника" )
    emb.add_field(name = "!!unban", value = "Вернуть доступ к серверу" )
    
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


token = open("token.txt", "r").readline()

client.run( token )



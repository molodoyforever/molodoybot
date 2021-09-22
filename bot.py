
import asyncio
import random
from re import U
from sys import prefix
import discord
from discord import activity
from discord import channel
from discord import embeds
from discord import colour
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
zabavi = ["админы норм?"]

#сказать
@client.command( pass_context = True)

async def сказать (ctx, *, arg):
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
        await message.channel.send("Пропиши команду +хелп для подробной информации.")
    
    if msg in poka:
        await message.channel.send("Надеюсь, увидимся ещё!")

    if msg in zabavi:
        await message.channel.send("Мой создатель лучший на свете!)")

#удалим сообщения
@client.command( pass_context = True)
@commands.has_permissions( administrator = True )

async def очистить(ctx, amount = 20):
    await ctx.channel.purge( limit = amount )

#help
@client.command( pass_context = True)
async def хелп( ctx ):
    emb = discord.Embed(title = "Навигация по командам")

    emb.add_field(name = "`+хелп`", value = "```Это сообщение```" )
    emb.add_field(name = "`+аватар`", value = "```Запросить свой/участника аватар```" )
    emb.add_field(name = "`+сказать`", value = "```Фраза от имени бота```" )
    emb.add_field(name = "`+очистить`", value = "```Очистка чата```" )
    emb.add_field(name = "`+обнять`", value = "```RP:Обнять участника сервера```" )
    emb.add_field(name = "`+поцеловать`", value = "```RP:Поцеловать участника сервера```" )
    emb.add_field(name = "`+убить`", value = "```RP:Убить участника сервера```" )
    emb.add_field(name = "`+лизнуть`", value = "```RP:Лизнуть участника сервера```" )
    emb.add_field(name = "`+погладить`", value = "```RP:Погладить участника сервера```" )
    emb.add_field(name = "`+тыкнуть`", value = "```RP:Тыкнуть участника сервера```" )
    emb.add_field(name = "`+укусить`", value = "```RP:Укусить участника сервера```" )
    emb.add_field(name = "`+курить`", value = "```RP:Покурить```" )
    
    await ctx.send( embed = emb )

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
    "https://media.giphy.com/media/u9BxQbM5bxvwY/giphy.gif",
    "https://c.tenor.com/Q83w83J1VzUAAAAC/hug-love.gif",
    "https://c.tenor.com/c8M8yU1q6c4AAAAC/hug-anime.gif"]
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
    "https://i.gifer.com/2lte.gif",
    "https://i.gifer.com/2ltq.gif"]
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
    embed = discord.Embed(description = f"{ctx.message.author.mention} покурил(а), {Notes}")
    embed.set_image(url=random.choice(smokeGifs))

    await ctx.send(embed=embed)

#тыкнуть 
@client.command()

async def тыкнуть( ctx, user: discord.User, *, Notes):
    await ctx.channel.purge(limit = 1)
    pokeGifs = ["https://i.gifer.com/FK0b.gif",
    "https://i.gifer.com/S00v.gif",
    "https://i.gifer.com/Lqge.gif",
    "https://i.gifer.com/SKql.gif",
    "https://i.gifer.com/QIzc.gif",
    "https://i.gifer.com/HlJ6.gif"]
    embed = discord.Embed(description = f"{ctx.message.author.mention} тыкнул(а) {user.mention}, {Notes}")
    embed.set_image(url=random.choice(pokeGifs))

    await ctx.send(embed=embed)

#погладить 
@client.command()

async def погладить( ctx, user: discord.User, *, Notes):
    await ctx.channel.purge(limit = 1)
    patGifs = ["https://i.gifer.com/KJ42.gif",
    "https://i.gifer.com/AWA3.gif",
    "https://i.gifer.com/GJor.gif",
    "https://i.gifer.com/Ckuy.gif",
    "https://i.gifer.com/fybn.gif"]
    embed = discord.Embed(description = f"{ctx.message.author.mention} погладил(а) {user.mention}, {Notes}")
    embed.set_image(url=random.choice(patGifs))

    await ctx.send(embed=embed)

#укусить 
@client.command()

async def укусить( ctx, user: discord.User, *, Notes):
    await ctx.channel.purge(limit = 1)
    biteGifs = ["https://c.tenor.com/8UjO54apiUIAAAAC/gjbu-bite.gif",
    "https://media.giphy.com/media/4JpvyNYuyf0aI/giphy.gif?cid=ecf05e47nz2s4iss30wam7io9e2m7lbti0tmx1wt5wnx8o06&rid=giphy.gif&ct=g",
    "https://i.gifer.com/H3Jt.gif",
    "https://animesher.com/orig/0/94/941/9418/animesher.com_bite-gif-image-vampire-knight-941852.gif",
    "https://animesher.com/orig/0/83/836/8362/animesher.com_gif-funny-girl-836208.gif",
    "https://c.tenor.com/4j3hMz-dUz0AAAAC/anime-love.gif",
    "https://c.tenor.com/5FOgNEcoaYMAAAAC/neck-kisses.gif"
    "https://c.tenor.com/1LtA9dSoAIQAAAAC/zero-no-tsukaima-bite.gif"]
    embed = discord.Embed(description = f"{ctx.message.author.mention} укусил(а) {user.mention}, {Notes}")
    embed.set_image(url=random.choice(biteGifs))

    await ctx.send(embed=embed)

#аватар
@client.command()
async def аватар(ctx, *, member: discord.Member=None):
    await ctx.channel.purge(limit = 1)
    if not member:
        member=ctx.message.author
    userAvatar = member.avatar_url

    embed=discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Аватар {member}")
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"Запрошено {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


token = open( "token.txt", "r" ).readline()

client.run( token )



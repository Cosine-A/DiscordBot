import discord
from discord.ext import commands
from datetime import datetime

token = ""
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

main_channel = bot.get_channel(949892001355141123)
bot_channel = bot.get_channel(1014781433799266366)

@bot.event
async def on_ready():
    state_message = discord.Game("공방 관리")
    await bot.change_presence(status=discord.Status.online, activity=state_message)


@bot.command
async def 시간(ctx):
    now = datetime.now()
    time = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
    await ctx.send("현재 시간은 %s 입니다" % time)


@bot.event
async def on_member_join(member):
    message = "$s님 아카랑 공방에 오신 것을 환영합니다!" % member
    await main_channel.send(message)


@bot.event
async def on_message_delete(member, message):
    send = "{0}님이 ""{1}""의 내용의 메시지를 지웠습니다.".format(member, message)
    await bot_channel.send(send)


@bot.event
async def on_message_edit(member, before, after):
    send = "```cs \n {0}님이 메시지를 수정하였습니다. \n 처음 내용: {1} \n 바뀐 내용: {2} \n ```".format(member, before, after)
    await bot_channel.send(send)




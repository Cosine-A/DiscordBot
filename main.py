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


@bot.event
async def on_message(message):
    if "ㅅㅂ" in message.content:
        author = message.author.mention
        await message.delete()
        await message.channel.send(f"{author}님이 비속어를 사용하였습니다.")


@bot.command
async def 시간(ctx):
    now = datetime.now()
    time = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
    await ctx.send(f"현재 시간은 {time} 입니다")


@bot.event
async def on_member_join(member):
    message = f"{member}님 아카랑 공방에 오신 것을 환영합니다!"
    await main_channel.send(message)


@bot.event
async def on_message_delete(message):
    embed = discord.Embed(title=f"삭제됨", description=f"유저 : {message.author} \n 채널 : {message.channel.mention}", color=0xFF0000)
    embed.add_field(name="삭제된 내용", value=f"내용 : {message.content}", inline=False)
    embed.set_footer(text=f"{message.guild.name} | {time}")
    await bot_channel.send(embed=embed)


@bot.event
async def on_message_edit(before, after):
    author = before.author
    send = f"```cs \n {author}님이 메시지를 수정하였습니다. \n 처음 내용: {before} \n 바뀐 내용: {after} \n ```"
    await bot_channel.send(send)

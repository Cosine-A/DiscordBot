import discord
from discord.ext import commands
from datetime import datetime

TOKEN = 'MTAxNDc1MDkzNTEwNjQ3NDAwNA.GkavS3.TdsHr3_MNlDPHGDhddf7VUXGXjBaGzSTVzU_Xs'

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

now = datetime.now()

main_channel_id = 949892001355141123
test_channel_id = 1014858948559503481


@bot.event
async def on_ready():
    state_message = discord.Game("공방 관리")
    await bot.change_presence(status=discord.Status.online, activity=state_message)


@bot.event
async def on_message(message):
    if message.content.startswith("!청소 "):
        purge_number = message.content.replace("!청소 ", "")
        check_purge_number = purge_number.isdigit()

        if not check_purge_number:
            await message.channel.send("올바른 값을 입력해주세요.")
            return
        await message.channel.purge(limit=int(purge_number) + 1)
        await message.channel.send("메시지 청소함").delete()

@bot.command
async def time(ctx):
    now_time = f"{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초"
    await ctx.send(f"현재 시간은 {now_time} 입니다")


@bot.event
async def on_member_join(member):
    main_channel = bot.get_channel(main_channel_id)
    message = f"{member}님 아카랑 공방에 오신 것을 환영합니다!"
    await main_channel.send(message)


@bot.event
async def on_message_delete(message):
    bot_channel = bot.get_channel(test_channel_id)
    now_time = f"{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초"
    embed = discord.Embed(title=f"삭제된 메시지", description=f"유저: {message.author} \n 채널: {message.channel.mention}",
                              color=0xFF0000)
    embed.add_field(name="삭제된 내용", value=f"{message.content}", inline=False)
    embed.set_footer(text=f"{message.guild.name} | {now_time}")
    await bot_channel.send(embed=embed)


@bot.event
async def on_message_edit(before, after):
    bot_channel = bot.get_channel(test_channel_id)
    now_time = f"{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초"
    embed = discord.Embed(title=f"수정된 메시지",
                          description=f"유저: {before.author} \n 채널: {before.channel.mention}",
                          color=0xFF9900)
    embed.add_field(name="수정 전 내용", value=before.content, inline=True)
    embed.add_field(name="수정 후 내용", value=after.content, inline=True)
    embed.set_footer(text=f"{before.guild.name} | {now_time}")
    await bot_channel.send(embed=embed)


bot.run(TOKEN)

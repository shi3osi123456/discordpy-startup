from discord.ext import commands
import os
import traceback

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content == ('/coin'):
        mylist = [表,裏] 
        await message.channel.send(randdom.choice(1))

bot.run(token)

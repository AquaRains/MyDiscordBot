import asyncio
import discord
import botcommand

client = discord.Client()

token = 'NDc0ODQxMTk1MzcwMjUwMjUx.DkqbgQ.oJduLHlChh8pRVhuejIccUc9pa8'

# 봇이 구동되었을 때 동작되는 코드입니다.

client.messageecho = True

@client.event
async def on_ready():
    print("Logged in as ")  # 화면에 봇의 아이디, 닉네임이 출력됩니다.
    print(client.user.name)
    
    print(client.user.id)
    print("===========")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
    await client.change_presence(game=discord.Game(name="반갑습니다 :D", type=1))
    #messageecho = True

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.


@client.event
async def on_message(message):
    if message.author.bot:  # 만약 메시지를 보낸사람이 봇일 경우에는
        return None  # 동작하지 않고 무시합니다.

    id = message.author.id  # id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel  # channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.
    text = message.content


    if text.startswith('!'):
        if text.startswith('!커맨드'):
            await client.send_message(channel, '커맨드')
        elif text.startswith('!시발'):
            await client.send_message(channel, '욕하지마븅시나')
        elif text.startswith('!에코'):
            if client.messageecho:
                await client.send_message(channel, '메아리 모드를 끕니다')
            else:
                await client.send_message(channel, '메아리 모드를 켭니다')

            client.messageecho = not client.messageecho
        else:
            try:
                await client.send_message(channel,
                                        await message_operate(message.content))
            except Exception as b:
                await client.send_message(channel, '[' + text + ']라고? 그딴 명령어 읍는데요?')
                pass
    else:
        if client.messageecho:
            await client.send_message(channel,
                                "<@"+id+">님이 \""+message.content+"\"라고 말하였습니다.")


async def message_operate(command):
    t = botcommand.commandlist.keys()
    if command in t:
        res = await botcommand.runcommand(command)
        return res


client.run(token)

import discord
import asyncio

client- discord.client()

token = "ODU4NTQwMTE0MDQ5MTA1OTMw.YNfnyg.KXF2aiGFuRoiM6zt8r2CtDNMfHQ"

@client.event
async def on_ready():

    print(client.user.name)
    print('이귀봇 정상적으로 실행되었습니다.')
    game = discord.game ('잘생긴 이귀봇')
    await client.change_presence(status=discord.status.online, activity=(game)
    
    


    @client.event
    async def on_message(message): 
        if message.content == "이귀":
            await message.channel.send(안녕하세요 저는 이귀봇이라고 하고 주인장 이귀보다 잘생긴 놈이기에 구독과 좋아요를 눌르고 에릭이는 벌룬급이고 김냥코는 왕두리급 입니다 )

            client.run(token)

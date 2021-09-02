# by xadjilut, 2021

from .. import loader, utils

class AliasesMod(loader.Module):
	"""Модуль чисто для алиасов"""

	strings = {'name': 'Aliases'}
	
	def __init__(self):
		self.name = self.strings['name']

	async def client_ready(self, client, db):
		self.db = db
		self.client = client

	async def aliasescmd(self, message):
		"""Выводит список доступных сокращений команд (алиасов)"""
		t = "<b>Доступные сокращения:</b>\n\n"
		dbb = self.db.get('friendly-telegram.modules.corectrl', 'aliases')
		i = 0
		for x in dbb:
			i += 1
			t += f"• {x} --- {dbb[x]}\n"
		if i == 0:
			t += '<i>Список пуст</i>'
		await message.edit(t, parse_mode="HTML")
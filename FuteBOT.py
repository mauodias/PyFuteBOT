from datetime import datetime
from time import sleep
from twitter_handler import twitter_handler
from facebook_handler import facebook_handler

class FuteBOT:
	def __init__(self):
		try:
			json_file = open('config.json').read()
		except IOError:
			raise IOError('Error loading configuration file')
		
		self.tw = twitter_handler(json_file)
		self.fb = facebook_handler(json_file)
		
	def parse_command(self, command):
		commands = str(command).split('.')
		for command in commands:
			parts = command.split(':')
			if parts[0].upper()=='N':
				parameters = parts[1].split(' ')
				for parameter in parameters:
					description = parameter.split('_')
					if len(description)!=2:
						return {"error": "Command parameters must have two parts ('NAME_VALUE'): " + parameter}
					if description[0]=='D':
						if len(description[1])==8:
							date=datetime.strptime(description[1], '%d%m%Y')
						else:
							return {"error": "Dates must have 8 characters ('DDMMYYYY'): " + description[1]}
					if description[0]=='H':
						if len(description[1])==4:
							time={"hours":description[1][0:2], "minutes":description[1][2:4]}
						else:
							return {"error": "Time must have 4 characters ('HHMM'): " + description[1]}
					if description[0] not in ('D', 'H'):
						return {"error":"Invalid parameter description (Currently accepted: D_DDMMYYYY AND H_HHMM): " + parameter}
				return self.create_match(date, time)

	def create_match(self, date, time):
		message = {0:'Segunda', 2:'Terca', 2:'Quarta', 3:'Quinta', 4:'Sexta', 5:'Sabado', 6:'Domingo'}[date.weekday()]
		message += ', ' + str(date.day) + '/' + str(date.month)
		message += ', ' + str(time['hours']) + ':' + str(time['minutes']) + '.'
		return self.fb.post_to_feed(message)

	def start(self):
		while True:
			tweet = self.tw.pop_direct_message()
			if tweet is not None:
				parseresult = self.parse_command(tweet['text'])
				print(parseresult)
				'''
				if parseresult[0]=='error':
					self.tw.reply_direct_message(tweet['sender_id'], 'Error: ' + parseresult[1])
				else:
					self.tw.reply_direct_message(tweet['sender_id'], 'Command processed successfully: ' + tweet['text'])
					'''
			sleep(60)
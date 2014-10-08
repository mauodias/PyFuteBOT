from twitter_handler import twitter_handler
from facebook_handler import facebook_handler

class test:
	def __init__(self, json_file):
		self.tw = twitter_handler(open(json_file))
		self.fb = facebook_handler(open(json_file))

	def check(self):
		print('in func')
		message = None
		while message is None:
			print('message before: ' + str(message))
			message = self.tw.pop_direct_message()
			print('message after: ' + str(message))
			if message is not None:
				self.fb.post_to_feed('884210374923421',message)
				break	
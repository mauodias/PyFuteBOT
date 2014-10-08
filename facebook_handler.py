import facebook
import json

class facebook_handler:
	def __init__(self, json_file):
		self.config = json.loads(json_file)['facebook']
		token = self.config['token']
		self.api = facebook.GraphAPI(token)
		print('Facebook loaded successfully.')

	def post_to_feed(self, message):
		try:
			result = self.api.put_object(self.config['group'], 'feed', message=message)
		except Exception, e:
			return {'error':'Problem on posting to feed: ' + e.message}
		return result
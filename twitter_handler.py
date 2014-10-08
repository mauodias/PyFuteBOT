import json
import twitter

class twitter_handler:
    def __init__(self, json_file):
        keys = json.loads(json_file)['twitter']
        consumer_key = keys['consumer_key']
        consumer_secret = keys['consumer_secret']
        access_token_key = keys['access_token_key']
        access_token_secret = keys['access_token_secret']
        self.api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)
        print('Twitter loaded successfully.')

    def pop_direct_message(self):
        dms = self.api.GetDirectMessages()
        dms.sort(key=lambda dm:dm.created_at)
        try:
                dm = dms.pop()
                self.api.DestroyDirectMessage(dm.id)
                return {"text": dm.text, "sender_id": dm.sender_id, "created_at":dm.created_at}
        except IndexError:
                return None

    def reply_direct_message(self, user_id, message):
        replydm = self.api.PostDirectMessage(message, user_id)
        return {"text":replydm.text, "created_at":replydm.created_at}
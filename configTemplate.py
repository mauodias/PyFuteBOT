def __init__(self):
    self.twitter = twitter()
    self.facebook = facebook()
    self.core = core()

class twitter():
    consumer_key='CONSUMER_KEY'
    consumer_secret='CONSUMER_SECRET'
    access_token_key='ACCESS_TOKEN_KEY'
    access_token_secret='ACCESS_TOKEN_SECRET'

class facebook():
    token='TOKEN'
    group='GROUP_ID'

class core():
    loopTime=60
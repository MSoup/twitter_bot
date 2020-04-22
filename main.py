import tweepy, time, sys

argfile = str(sys.argv[1])

CONSUMER_KEY = 'AEuOnOkHFgbVmDzmP5eLkRoh5'
CONSUMER_SECRET = input("Wazza pass?")
ACCESS_KEY = '1165776405658886144-OeeOBkvQqpy01CW4QJxleWx3j3GLmD'
ACCESS_SECRET = input("Wazza access pass?")
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes
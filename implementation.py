from decouple import config
import tweepy
#todo: create a file with their names + loop through em + search + get task done + delete file

# Configuration stuff
###############################################
CONSUMER_KEY = config('CONSUMER_KEY')
SECRET_KEY = config('SECRET_KEY')
ACCESS_TOKEN_ONE = config('ACCESS_TOKEN_ONE')
ACCESS_TOKEN_TWO = config('ACCESS_TOKEN_TWO')
###############################################

# GLOBAL API object




# Authenticate to Twitter API
def O_Auth():

    # here goes the consumer key and secret
    auth = tweepy.OAuthHandler(CONSUMER_KEY,
    SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN_ONE,
    ACCESS_TOKEN_TWO)

    API = tweepy.API(auth, wait_on_rate_limit=True,
                       wait_on_rate_limit_notify=True)

    #check if consumer and secret key are key being requested correctly
    try:
        redirect_url = auth.get_authorization_url()
        print("\t\n [*][*][*] Authentication went through succesfully [*][*][*]\n")
    except tweepy.TweepError:
        print('Error! Failed to get request token.')
    #fetching user
    #user_id = 'elonmusk'
    #user = api.get_user(user_id)
    #print("user ID: ", user.id_str)
    return API


def get_twitter_user_id():
    api = O_Auth()
    #ASK USER FOR TWITTER NAME
    user_id = input("ENTER TWITTER NAME: ").lower()

    if user_id[0] == '@':
        user_id = user_id.replace("@","")

    ID = api.get_user(user_id)


    return ID.id_str
    #timeline = api.user_timeline(user_id)
    #api.update_status(user_id + " hello")






def reply(user_id):
    #create a tweet
    pass



def retweet(user_id, count=1):
    pass

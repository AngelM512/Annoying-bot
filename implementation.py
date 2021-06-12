from decouple import config
import tweepy
import time
#todo: create a file with their names + loop through em + search + get task done + delete file

# Configuration stuff
###############################################
CONSUMER_KEY = config('CONSUMER_KEY')
SECRET_KEY = config('SECRET_KEY')
ACCESS_TOKEN_ONE = config('ACCESS_TOKEN_ONE')
ACCESS_TOKEN_TWO = config('ACCESS_TOKEN_TWO')
###############################################

# Authenticate to Twitter API
def API_PLUS_O_AUTH():

    # here goes the consumer key and secret
    auth = tweepy.OAuthHandler(CONSUMER_KEY,SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN_ONE, ACCESS_TOKEN_TWO)

    #API object
    API = tweepy.API(auth, wait_on_rate_limit=True,
                       wait_on_rate_limit_notify=True)

    #check if consumer and secret key are key being requested correctly
    try:
        redirect_url = auth.get_authorization_url()
        print("\t\n [*][*][*] Authentication went through succesfully [*][*][*]\n")
    except tweepy.TweepError:
        print('Error! Failed to get request token.')

    return API


def get_twitter_user_data():

    #call func that gets twitter API ready
    api = API_PLUS_O_AUTH()

    #ASK USER FOR TWITTER NAME
    user_id = input("ENTER TWITTER NAME: ").lower().replace(" ", "")

    if user_id[0] == '@':
        user_id = user_id.replace("@","")

    # get me the id of the user provided + its most recent data
    user_data = api.get_user(user_id)

    #what to do when user is not found?
    while True:
        try:
            print("User was found")
            time.sleep(2)
        except tweepy.TweepError as error:
            print("\n\nUser not found, try again")
            if error[0]['code'] == 50 or error[0]['message'] == 'User not found.':
                user_id = input("ENTER TWITTER NAME: ").lower().replace(" ", "")
                ID = api.get_user(user_id)
                pass
        break

    return user_data #returns the whole Json file with user's info


def get_latest_reply_id_and_message(data):
    print(data)
    #get tweet ID
    tweet_id = data.status.in_reply_to_status_id
    print("[*****]tweet_id = ", tweet_id, " data type= ", type(tweet_id))

    #get latest message posted
    latest_message = data.status.text

    #store data and return
    message_plus_tweetId = {
                            'tweet_id': tweet_id,
                            'message': latest_message
                            }

    return message_plus_tweetId


def reply(data):
    #data.update_status()
    pass
    #create a tweet

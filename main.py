#!/usr/bin/env python3
from implementation import *

#main program function
def main():
    API = API_PLUS_O_AUTH()
    # get the user twitter id user you want to mimic
    # user must be provided like: @user123
    data = get_twitter_user_data(API)
    print( "\n\n\n\n\n" )

    # get_latest_reply_id_and_message returns a dictionary with
    # the tweet id and the user's latest reply
    tweet_and_message_dict = get_latest_reply_id_and_message(data)




    #reply users latest tweet
    #reply(tweet_and_message_dict, API)


main()

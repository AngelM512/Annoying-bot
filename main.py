from implementation import *

#main program function
def main():
    # get the user twitter id user you want to mimic
    # user must be provided like: @user123
    data = get_twitter_user_data()
    print("\n\n\n\n\n")
    print('get_lattest_reply= ',get_latest_reply_id_and_message(data))

    #reply users latest tweet
    #reply()


main()

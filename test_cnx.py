import tweepy
from pprint import pprint

 
# API keyws that yous saved earlier
api_key = "dLLh0WfotPhJlWehKRcdUrDIC"
api_secrets = "bcRbRiSo9bx5ttflrJjVzn9y06Y7TF9QLK2ZNZMMtNKSBOu7zE"
access_token = "2985691582-BvNFompzEs57kZKTXmKAg5fP6B7kOEY53bLmcAm"
access_secret = "3QgvYoBRXs8ryByzcQxCRzWU4e3Qaioe1KkNZm5MQKGXW"

# api_key = "HmxyniLUdBhpRZNGhMzS7FiYm"
# api_secrets = "ijT2j4u08b0c3ZwSDv0OAe3EBtm5S9Db7obhGOYdvoX2h96hdH"
# access_token = "2985691582-FjXn1N7JzyT4sdY2r8BAqkgKqIt57nAyaMtyKkL"
# access_secret = "1OVJdnROseAQgk2atk4ZbbroicVi7SiiK4O3x2QT7TY3E"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
 
api = tweepy.API(auth)
 
try:
    api.verify_credentials()
    print('Successful Authentication')
    user = api.get_user(screen_name='gerardotc')
    print(f"user.name: {user.name}")
    print(f"user.screen_name: {user.screen_name}")
    print(f"user.location: {user.location}")
    print(f"user.description: {user.description}")
    print(f"user.followers_count: {user.followers_count}")
    print(f"user.listed_count: {user.listed_count}")
    print(f"user.statuses_count: {user.statuses_count}")
    print(f"user urls: {user.entities['url']['urls'][0]['expanded_url']}")
    #pprint(user._json)



except Exception as e:
    print(e.args)
    print('Failed authentication')

# API key: dLLh0WfotPhJlWehKRcdUrDIC
# API secret key: bcRbRiSo9bx5ttflrJjVzn9y06Y7TF9QLK2ZNZMMtNKSBOu7zE

# Access token: 2985691582-BvNFompzEs57kZKTXmKAg5fP6B7kOEY53bLmcAm
# Access token secert: 3QgvYoBRXs8ryByzcQxCRzWU4e3Qaioe1KkNZm5MQKGXW

# API key: HmxyniLUdBhpRZNGhMzS7FiYm
# API secret key: ijT2j4u08b0c3ZwSDv0OAe3EBtm5S9Db7obhGOYdvoX2h96hdH
# Access token: 2985691582-FjXn1N7JzyT4sdY2r8BAqkgKqIt57nAyaMtyKkL
# Access token secret: 1OVJdnROseAQgk2atk4ZbbroicVi7SiiK4O3x2QT7TY3E
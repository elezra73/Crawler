from __future__ import absolute_import, print_function

import ssl
import time

import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
from pip._internal.utils import logging
from tweepy import TweepError

#consumer_key="fUQPJu7goniR2hfi5R5Klwtrn"       #machine learning , old
#consumer_secret="JpApHOlXEfBxqoGggPZux6kRhLSnLAHhcMRq12K6yiXsUS86qf"   # machine learning , old
from requests import Timeout
from urllib3.exceptions import ReadTimeoutError, ConnectionError, SSLError

consumer_key = "8h2gg259CNETqZNR9xq3Z1u3X"      #new Key Data Retriveal
consumer_secret = "TVv2tjVSmJJzMRpyWkbW4k3A2lDoSTPbXioRbtmobPPKVHytyP"      #new Key Data Retriveal


# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
#access_token="1003222000523993089-6QBWMQBTNtiVz7NrtcBw3PTigQlpjJ"       #old
#access_token_secret="rRrKrD5W7LhmwminPcQHzGJJei5D22xnnvfEJcxONTsEn"     #old

access_token = "1003222000523993089-nN73BpEgT4T80q8argxts6trocQAva"
access_token_secret = "p0DlLZK9AmJjrYq4fBhJBzhMbmytvG2HvAMfUwgQFqUrV"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

Tweets = open("Tweets.txt", "w")
# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)


# The Twitter user who we want to get tweets from
name = "Sandisk"
# Number of tweets to pull
tweetCount = 25
#print(r = api.followers(api.me().name))

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
c = tweepy.Cursor(api.followers, id=name).items()
#print ("type(c)=", c)
file = open("Sandisk.txt" , 'w')
i = 0

for user in tweepy.Cursor(api.followers, id = name).items():
    try:
       # file.write(str(user))
        #print ("user name = " + user.screen_name.encode(encoding="utf-8" , errors = "strict")+ "user location = " + user.location.encode(encoding = "utf-8" , errors = "strict"))
        if(user.location != ""):
            i= i + 1;
            print(i);
        file.write(user.screen_name.encode(encoding="utf-8", errors="strict")
            +";"+ '%1s' % user.location.encode(encoding="utf-8", errors="strict")
            +";"+ '%1s' % str(user.created_at)
            +";"+ '%1s' % str(user.followers_count) + '\n')
        time.sleep(0.5)
        #if(i==20):
        #    break

    except tweepy.TweepError:
         time.sleep(60 * 15)
         continue
    except (Timeout, SSLError, ReadTimeoutError, ConnectionError) as e:
        logging.warning("Network error occurred. Keep calm and carry on.", str(e))
    except Exception as e:
        logging.error("Unexpected error!", e)
    except TweepError as e:
        if 'Failed to send request:' in e.reason:
            print("Time out error caught.")
        time.sleep(180)
        continue
    except:
        print("blat")
        time.sleep(60)
        continue
file.close()
# for follower in c:
#     #ids.append(follower)
#     file.write(str(follower))
#     print(follower)
#     file.write('\n')
#     time.sleep(60)


list_of_users = []


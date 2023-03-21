'''
Instagram Following Non-followers
Created Date: 01/21/23
Checks Instagram account followings to discover which followings are not following back the account.

Created by: Johnson Le
'''

import json

# Converts JSON files to Python in order to read
with open('following.json') as file:
    following_json = json.load(file)

with open('followers.json') as file:
    followers_json = json.load(file)

# Adds users from account's followers to a list of followers
users_not_following = []
for following in following_json["relationships_following"]:
    users_not_following.append(following["string_list_data"][0]["value"])

# Calculates the differences of account's followings versus account's followers
for follower in followers_json["relationships_followers"]:
    follower = follower["string_list_data"][0]["value"]
    if follower in users_not_following:
# Resulting only users with no mutual connections of users not following back the account
        users_not_following.remove(follower)

# Displays results
print("Users who don't follow back:")
for user in users_not_following:
    print("- @" + user)
import json

# Load followers
f = open('followers_1.json')
data = json.load(f)

followers = []

for i in data:
    for j in i['string_list_data']:
        followers.append(j['value'])

# Load following
f = open('following.json')
data = json.load(f)

following = []

for i in data["relationships_following"]:
    for j in i['string_list_data']:
        following.append(j['value'])

# Find people you follow but who don't follow you back
not_following_back = []

for i in following:
    if i not in followers:
        not_following_back.append(i)

# Print the list of those who don't follow you back
for i in not_following_back:
    print("https://www.instagram.com/" + i)

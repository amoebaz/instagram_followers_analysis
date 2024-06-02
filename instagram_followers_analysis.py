# Instagram Followers Analysis

import json
import os.path


following = "./instagram_download/connections/followers_and_following/following.json"
followers = "./instagram_download/connections/followers_and_following/followers_"

# We search for all followers files
i = 1
followers_current = followers + str(i) + ".json"
print(followers_current)
followers_json = list()

while os.path.isfile(followers_current):
    with open(followers_current) as f:
        followers_json.extend(json.load(f))
        i += 1
        followers_current = followers + str(i) + ".json"

#print (len(followers_json))

with open(following) as f:
    following_json = json.load(f)

#for z in range(len(followers_json)):
#    print(followers_json[z]['string_list_data'][0]['value'])

prueba = list()
total = 0
for i in range(len(following_json['relationships_following'])):
    follow_back = False
    for z in range(len(followers_json)):
        if (following_json['relationships_following'][i]['string_list_data'][0]['value'] == followers_json[z]['string_list_data'][0]['value']):
#            print(followers_json[z]['string_list_data'][0]['value'])
            follow_back = True
            break
    if follow_back == True:
        print(following_json['relationships_following'][i]['string_list_data'][0]['value'])
        total += 1
        prueba.extend(following_json['relationships_following'][i]['string_list_data'][0]['value'])

print (total)

#    print(following_json['relationships_following'][i]['string_list_data'][0]['value'])

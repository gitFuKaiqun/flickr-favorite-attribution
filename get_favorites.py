import pickle

import flickrapi

from config import (
    FLICKR_KEY, FLICKR_SECRET)


USERNAME_DICT_FILENAME = "username_dict.p"

flickr = flickrapi.FlickrAPI(FLICKR_KEY, FLICKR_SECRET)

# authorize script (it opens web browser)
# this needs to be done only once
(token, frob) = flickr.get_token_part_one(perms='write')
if not token:
    raw_input("Press ENTER after you authorized this program")
    flickr.get_token_part_two((token, frob))

# `username_dict` - dict that stores username for userid
try:
    username_dict = pickle.load(open(USERNAME_DICT_FILENAME, "rb"))
except Exception, e:
    username_dict = {}
    if 'No such file' in e:
        print 'Pickle file for username_dict does not exist, it will be created'

# TODO: extend for the case of several pages of favorites
favorites = flickr.favorites_getList(per_page=500)
photos = favorites.findall('./photos/photo')
names_list = []
for p in photos:
    # owner is ID not username
    owner = p.attrib['owner']
    print 'id: ', owner
    username = username_dict.get(owner, None)
    if not username:
        userinfo = flickr.people_getInfo(user_id=owner)
        username = userinfo.findall('./person/username')[0].text
        username_dict[owner] = username
    print 'username: ', username
    names_list.append(username)

# save file `names.txt`
with open('names.txt', 'w') as f:
    for n in names_list:
        f.write(n.encode('utf8') + '\n')

# save username_dict not to run getInfo queries later
pickle.dump(username_dict, open(USERNAME_DICT_FILENAME, "wb"))

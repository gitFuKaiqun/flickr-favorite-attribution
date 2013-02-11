import sys
import os
from xml.etree.ElementTree import tostring

import flickrapi

from config import (
    FLICKR_KEY, FLICKR_SECRET,
    CLOUD_IMAGE_FILENAME)


flickr = flickrapi.FlickrAPI(FLICKR_KEY, FLICKR_SECRET)

# authorize script (it opens web browser)
# this needs to be done only once
(token, frob) = flickr.get_token_part_one(perms='write')
if not token:
    raw_input("Press ENTER after you authorized this program")
    flickr.get_token_part_two((token, frob))

if not os.path.exists(CLOUD_IMAGE_FILENAME):
    print 'Image file %s does not exist' % CLOUD_IMAGE_FILENAME
    sys.exit()

resp = flickr.upload(
    filename=CLOUD_IMAGE_FILENAME,
    title='Word cloud of users I favorited',
    tags='''flickr favorites "word cloud"''',
    format='etree')

# print response
print tostring(resp)

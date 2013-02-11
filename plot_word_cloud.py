import numpy as np

from word_cloud.wordcloud import make_wordcloud

from config import (
    WIDTH, HEIGHT,
    CLOUD_IMAGE_FILENAME)

# get word counts
count = {}
with open('names.txt') as f:
    for line in f:
        username = line[:-1]
        count[username.decode('utf8')] = count.get(username, 0) + 1
words = np.array(count.keys())
counts = np.array(count.values())

make_wordcloud(
    words, counts,
    CLOUD_IMAGE_FILENAME,
    width=WIDTH,
    height=HEIGHT,
    font_path="OldSansBlack.ttf", redraw_in_color=False)

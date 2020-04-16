"""
yt2rss.py

supply it with a file of youtube channel urls (in same directory)
and it will spit out a file with links to drop into any RSS
reader (the file is rss.txt and it will also be in the same directory)

@author C. J. Burton
@version 2020.04.16
"""

import sys
import os
from os import path

# url_file = open(sys.argv[1], 'r')
if path.exists('rss.txt'):
    os.remove('rss.txt')
rss_file = open('rss.txt', 'w')


def to_rss(yturl):
    return 'https://www.youtube.com/feeds/videos.xml?channel_id=' + yturl.split('/')[4]


with open(sys.argv[1]) as file_in:
    lines = []
    for line in file_in:
        temp = to_rss(line)
        rss_file.write(temp)
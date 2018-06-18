#! /usr/bin/env python3

import fileinput

"""
Script to parse URLs and hashtags out of tweet collection
"""

# make a set of most common URI schemes and hashtag 
search_strings = {'https:', 'http:', 'ftp:', 'file:', '#'}
for line in fileinput.input():
        # split by whitespace to get all words in line
        words = line.rstrip().split(' ')
        for word in words:
                # check to see if word starts with URI scheme or hashtag
                # and print all matches 
                for search_string in search_strings:
                        if word.startswith(search_string):
                                print(word)
                                break        

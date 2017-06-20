#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""myfeedparser 0.0.1

Usage:
    feed
    feed <rss-url>
    feed -b

"""

# from __future__ import print_function
import feedparser
import sys
from feedclass import Feedclass
import shelve
import re
from docopt import docopt

def print_feed(feed):
	d = feedparser.parse( feed.url )

	zipped = dict(enumerate(d.entries))

	for i,post in zipped.items():
	    print str(i+1) + " " + post.title 
	    print post.link + " "
	    print

def add_feed(url):
	data = shelve.open("allfeeds.db","n")
	name = raw_input("Enter feed name: ")
	newfeed = Feedclass(name,url)
	flag = True
	for key,val in data.iteritems():
		if(val == newfeed.url):
			print "ALREADY PRESENT WITH THE NAME: " + key
			print
			flag = False
			oldfeed = Feedclass(key,val)
			print_feed(oldfeed)
	if(flag == True):
		data[newfeed.name] = newfeed.url
		print_feed(newfeed)

def show_feeds():
	data = shelve.open("allfeeds.db","n")
	for key,val in data.iteritems():
		print key
	selectfeed = raw_input("Enter name of feed you wish to see: ")
	newfeed = Feedclass(selectfeed,data[selectfeed])
	print_feed(newfeed)

def main():
    args = docopt(__doc__, version='0.0.1')

    # parse args
    browse = args['-b']
    external = args['<rss-url>']
    
    fetch = True

    # get rss urls
    if external:
        add_feed(external)
    else:
        show_feeds()

# start
if __name__ == '__main__':
    main()
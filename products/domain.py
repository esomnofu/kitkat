"""
A HELPER FILE
=============
DOMAIN FUNCTIONS DEFINED HERE
HELPS EXTRACT THE DOMAIN NAME FROM A URL
THIS WILL HELP US WHEN CREATING FOLDERS 
FOR DIFFERENT  SITES WE WILL CRAWL
"""
from urllib.parse import urlparse


def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.')
		if len(results[-1]) == 2:
			return results[-3] +'.'+results[-2] +'.'+ results[-1]
		return results[-2] +'.'+ results[-1]
	except:
		return ''


def get_sub_domain_name(url):
	try:
		return urlparse(url).netloc
	except:
		return ''


'''
The get_all_item_links_by_sub_category uses the HomeCrawler Class
Gets the Major Categories
Create Folders by Name for All Major Categories inside the Main Project Folder i.e(jumia.com.ng)
Creates a txt File to Store All Products Links by Name for All Major Categories
Crawls All the Major Categories
Add All the Product Links in the Appropriate Text File
'''

#Import Modules Needed
import os
from lxml import html
import requests
from products.domain import *
#import datetime
#from products.get_all_major_category_links import HomeCrawler
#from products.detailed_view import DetailCrawler
#from products.general import *
#import time



#Each Category Crawler Class
class CategoryCrawler(object):
	
	#Initialization Method
	def __init__(self, starting_url, start_page_number, end_page_number, concatenation, product_url):
		#Each Category URL Passed in
		self.starting_url = starting_url

		#A Set of Unique Items for All Links in Each Category
		self.items = set()
		self.start_page_number = int(start_page_number)
		self.end_page_number = int(end_page_number)
		#self.pagination_index = pagination_index

		#Concatenation - I.E How to Navigate Through Each URL
		self.concatenation = concatenation


		self.product_url = product_url

		#A Counter to Help Iterate over All Pages in Each Category Initialize to 1
		self.page = 1

		#This is a Counter that Holds Current Page we are Crawling at Each Category Page we still just initialize to 1
		self.counter = ''

		self.project = get_domain_name(starting_url)


	#To String Method Returns all items
	def __str__(self):
		return('All Items:', self.items)


	#The Crawl Function
	def crawl(self):

		#If no Pagination index is provided the program ignores to crawl all the webpages
		#And instead crawls only the specified page interval
		#It first of all gets the maximum pagination number
		#self.get_max_pagination_link(self.starting_url)
		if self.counter != '':
			#And Loops through it while there are still pages available
			while self.page <= self.counter:
				#Gets all URLS of each products per category
				self.get_item_from_link(self.starting_url)
		else:
			#This is when only some specified page intervals are to be crawled
			#we now set the page used in the url as the self.start_page_number
			#self.page = self.start_page_number
			while self.start_page_number <= self.end_page_number:
				self.get_item_from_selected_links(self.starting_url)

		return

	#Method to get maximum pagination number
	def get_max_pagination_link(self, link):
						
			start_page = requests.get(link)

			tree = html.fromstring(start_page.text)

			pagination = tree.xpath(self.pagination_index)
				
			self.counter = int(pagination[-1])

			

	#Method to Gather All URLs of each product in each category
	def get_item_from_link(self, link):
				
			start_page = requests.get(link + self.concatenation + str(self.page))		

			tree = html.fromstring(start_page.text)

			links = tree.xpath(self.product_url)
		
			for link in links:
				self.items.add(link)
			self.page += 1
			

	#Method to Gather All URLs of each product in each category
	def get_item_from_selected_links(self, link):
				
			start_page = requests.get( link + self.concatenation + str(self.start_page_number) )		

			tree = html.fromstring(start_page.text)

			links = tree.xpath(self.product_url)
		
			for link in links:
				#Fix For DelphiMetals
				if ('http' not in link) and (self.project not in link):
					link = 'http://'+self.project+'/'+link
				self.items.add(link)
			self.start_page_number += 1




"""
================================================================================================================================================================================================
================================================================================================================================================================================================
================================================================================================================================================================================================
OUTSIDE THE CLASS
OUTSIDE THE CLASS
OUTSIDE THE CLASS
================================================================================================================================================================================================
================================================================================================================================================================================================
================================================================================================================================================================================================
"""


	


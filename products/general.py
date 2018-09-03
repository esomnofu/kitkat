"""
A HELPER FILE
=============

Helps us in creating new files
writing contents of lists or sets to a file
writing contents in a file to lists or sets
"""
import json
import requests
import random
import datetime
import os
from django.conf import settings

#Paginator Module
from django.core.paginator import Paginator, EmptyPage, InvalidPage



#Import Models Here

from products.models import Product, News

#Get Object or 404
from django.shortcuts import get_object_or_404



#Function to Write to Newly Created File...
def write_file(file_name, content):
	f = open(file_name, 'w')
	f.write(content)
	f.close() 

#This Function Helps Pickup all the Links From File and Store in Set for faster Operations at Run Time
def file_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as f:
		for line in f:
			results.add(line.replace('\n', ''))
	return results


#This Function is called to write links in the set to the appropriate file
def set_to_file(links, file):
	for link in sorted(links):
		append_to_file(file, link)


#Function to Append more links to existing file
def append_to_file(file_name, content):
	with open(file_name, 'a') as file:
		file.write(content + '\n')



#This Function is called to return an item in a list
#Its Meant Specifically For the Detail_view File
#Since the Attributes of Each item returns a list instead of string
def list_to_string(list):
	for item in list:
		if item is None:
			return "Not Assigned"
		else:
			return item.strip()


def description_availability(list):
	if list == []:
		return "No Description Available"
	else:
		result = ''
		for item in list:
			result += item.strip() + " "
		return result


def list_items_to_string(list):
	#Fix For Fashpa
	new_list = set()

	for item in list:
		new_list.add(item)
	#End Fix Fashpa

	result = ""
	for item in new_list:
		#Fix For baffshqboutique.com
		if ('Please' not in item) and ('Select' not in item):
			result += item.strip() + " "
		else:
			continue
	return result



def filter_list_colors(list):
	if list == []:
		return ["Not Available in Colors"]
		
	result = []
	for item in list:
		#Fix For baffshqboutique.com
		if ('Choose' not in item) and ('option' not in item):
			result.append(item.strip())
		else:
			continue
	return result


def list_items_to_categories(list):
	result = ""
	for item in list:
		result += item.strip() + ","
	return result




def old_price_availability(list):
	if list == []:
		return "No Old Price"
	else:
		for item in list:

			#Fix For DELUXE for Old and New Price
			ditem = str(item).split()
			if len(ditem) > 1:
				item_new_price = ditem[1]

				#Fix For DELUXE for Old and New Price
				if '₦' in item_new_price:
					item_new_price = item_new_price.strip()
					item_new_price = item_new_price[1:]
					return item_new_price

			if ('₦' in item) and ('.' in item):
				item = item.strip()
				item = item[1:-3]
				return item
			elif ('N' in item) and ('.' in item):
				item = item.strip()
				item = item[1:-3]
				return item
			elif '.' in item:
				item = item.strip()
				item = item[:-3]
				return item
			elif '₦' in item:
				item = item.strip()
				item = item[1:]
				return item
			elif 'N' in item:
				item = item.strip()
				item = item[1:]
				return item
			else:
				return item





def current_price_availability(list):
	for item in list:
		ditem = str(item).split()
		if len(ditem) > 1:
			item_new_price = ditem[1]
			#Fix For DELUXE for Old and New Price
			if '₦' in item_new_price:
				item_new_price = item_new_price.strip()
				item_new_price = item_new_price[1:]
				return item_new_price
			else:
				return item_new_price
		if ('₦' in item) and ('.' in item):
				item = item.strip()
				item = item[1:-3]
				return item
		elif ('N' in item) and ('.' in item):
			item = item.strip()
			item = item[1:-3]
			return item
		elif '.' in item:
			item = item.strip()
			item = item[:-3]
			return item
		elif '₦' in item:
			item = item.strip()
			item = item[1:]
			return item
		elif 'N' in item:
			item = item.strip()
			item = item[1:]
			return item
		else:
			return item

			

def sizes_availability(list):
	if list == []:
		return "Not Available in Sizes"
	else:
		return list

def off_availability(list):
	if list == []:
		return "No Discount Available"
	else:
		for item in list:
			if 'Save' in item:
				return item[5:]
			return item[1:]

def seller_availability(list):
	if list == []:
		return "No Seller"
	else:
		for item in list:
			return item

def get_valid_images(list):
	random_number = random.randint(500000000,1000000000)

	new_list = ""
	for image in list:
		
		#Start Fix For Fashpa
		if 'http' not in image:
			image = 'http:' + image
		#End Fix For Fashpa
		
		#Fix For Amaget
		image	= image.replace('-small_default', '-large_default')
		#End Fix for Amaget
		if ('.jpg' in image)  or ('.jpeg' in image) or ('.JPG' in image) or ('.png' in image) or ('.PNG' in image):
			response = requests.get(image)
			if response.status_code == 200:
				image_name = str(random_number) + ".jpg"
				with open('products/static/products/images/'+ str(datetime.date.today()) +'-'+ image_name, "wb")  as f:
					f.write(response.content)
					f.close()
					new_list+=(str(datetime.date.today()) +'-'+ image_name)+ " "
					random_number += 1
	return new_list


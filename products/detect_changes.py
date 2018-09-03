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


def news(arg, argz):

	#To Get The Last File in Media Directory
	path = arg
	#path = '/Users/DIAMONDSCRIPTS/Desktop/django/catalogue/media'

	#Getting the last TXT Files
	text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
	last = text_files[-1]

	
	#Loading the file up as a json so we can manipulate the Data
	with open(os.path.join(settings.NON_STATIC_ROOT+argz, last)) as json_file:
		data = json.load(json_file)
		for p in data['product']:

			product_name = p['name']
			product_seller = p['seller']
			product_old_price = p['old_price']
			product_current_price = p['current_price']
			product_url = p['url']
			product_categories = p['categories']
			product_valid_sizes = p['valid_sizes']
			product_off = p['off']
			product_valid_images = p['valid_images']
			product_color = p['color']
			product_description = p['description']

			#Check if This Product is Already in Database
			old_item = Product.objects.filter(product_url=product_url).count()
			#print('Count of IF item exists in Product Table = ', old_item)

			if old_item is 0:
				#Item is not in Database so we save new entry into Products and News Table
				each_table_row = Product( product_name=product_name, product_seller=product_seller, product_old_price=product_old_price, product_current_price=product_current_price, product_url=product_url, product_categories=product_categories.split(','), product_valid_sizes=product_valid_sizes.split(), product_off=product_off, product_valid_images=product_valid_images.split(), product_color=product_color, product_description=product_description )
				each_table_row.save()

				news_item = News( product_name=product_name, product_seller=product_seller, product_old_price=product_old_price, product_current_price=product_current_price, product_url=product_url, product_categories=product_categories.split(','), product_valid_sizes=product_valid_sizes.split(), product_off=product_off, product_valid_images=product_valid_images.split(), product_color=product_color, product_description=product_description)
				news_item.save()
				
				"""
				CHECK FOR CHANGES BEGINS
				CHECK FOR CHANGES BEGINS
				CHECK FOR CHANGES BEGINS
				"""
			else:

				"""
				ITEM IS ALREADY IN PRODUCT TABLE SO WE CHECK IF THERE IS ANY CHANGE TO ANY FIELD OF THIS PRODUCT
				ITEM IS ALREADY IN PRODUCT TABLE SO WE CHECK IF THERE IS ANY CHANGE TO ANY FIELD OF THIS PRODUCT
				ITEM IS ALREADY IN PRODUCT TABLE SO WE CHECK IF THERE IS ANY CHANGE TO ANY FIELD OF THIS PRODUCT
				CHECK FOR CHANGES BEGINS
				CHECK FOR CHANGES BEGINS
				CHECK FOR CHANGES BEGINS
				"""

				#Item Exists in the Database --- So we grab the old existing product from the Database

				#get_object_or_404 gets the product or return 404
				this_item = get_object_or_404(Product, product_url=product_url)
				#print('Get the Old item from Product Table or 404 = ', this_item)

				#Calling the detect_changes function of the Product Model Class
				#This Method returns an Array of all properties of this Table
				arr_item = this_item.detect_changes()
				#print('Getting the Fields We Want From this Old Item arr_item Contains = ', arr_item)				
				"""
				CHECK IF THERE IS ANY CHANGE IN PRICE FOR EXISTING PRODUCTS BEGINS
				CHECK IF THERE IS ANY CHANGE IN PRICE FOR EXISTING PRODUCTS BEGINS
				CHECK IF THERE IS ANY CHANGE IN PRICE FOR EXISTING PRODUCTS BEGINS				
				"""
				#Pick up old price from the arr_item which we returned on line 85 which contains the existing record from Product Table 
				old_item_current_price = arr_item[0]
				#Remove Commas From Old Price
				old_item_current_price	= old_item_current_price.replace(',', '')
				#Make Price an Integer thus suitable for making Comparison
				old_item_current_price = int(old_item_current_price)


				#Format the New Incoming Product also to make suitable for comparison
				new_item_current_price = product_current_price.replace(',', '')
				new_item_current_price = int(new_item_current_price)
				#Now Compare if there is any PRICE CHANGE

				#If there is a Drop in Price - We Execute This
				if old_item_current_price > new_item_current_price:
					#if price in database is bigger than incoming price, there is a price slash....
					#we can capture this by updating or adding this entry in our News Table

					#Check if it exists in News Table
					news_item = News.objects.filter(product_url=product_url).count()						
					#print('Checking New Compared Item URL existence in News Table Returns the Number = ', news_item)

					#Check if the entry is already in News Table						
					news = product_name + ' price has reduced from ' + str(old_item_current_price) + ' Naira to ' + str(new_item_current_price) + ' Naira'
					if news_item == 1:
						#Update that existing entry
						news_item.update( product_old_price=old_item_current_price, product_current_price=new_item_current_price, product_categories=product_categories.split(','), product_news=news, product_price_change_type='down', product_valid_images=product_valid_images.split() )
						#news_item.update( product_name=product_name, product_seller=product_seller, product_old_price=old_item_current_price, product_current_price=new_item_current_price, product_url=product_url, product_categories=product_categories.split(','), product_news=news, product_price_change_type='down', product_valid_images=product_valid_images.split() )
						
						#We Also Update Product Database for the same entry
						product_item = Product.objects.filter(product_url=product_url)
						product_item.update( product_old_price=old_item_current_price, product_current_price=new_item_current_price, product_categories=product_categories.split(','), product_valid_images=product_valid_images.split() )
						#product_item.update( product_name=product_name, product_seller=product_seller, product_old_price=old_item_current_price, product_current_price=new_item_current_price, product_url=product_url, product_categories=product_categories.split(',') )

					else:
						#We Add a Fresh Record to the News Table
						news_item = News( product_name=product_name, product_seller=product_seller, product_old_price=old_item_current_price, product_current_price=new_item_current_price, product_url=product_url, product_categories=product_categories.split(','), product_valid_sizes=product_valid_sizes.split(), product_off=product_off, product_valid_images=product_valid_images.split(), product_news=news, product_price_change_type='down', product_color=product_color )
						news_item.save()
						#print('Added a New Item that was in Product Table but was not in News Table - Price Down')
						#news_item = News( product_old_price=old_item_current_price, product_current_price=new_item_current_price, product_categories=product_categories.split(','), product_valid_sizes=product_valid_sizes.split(), product_off=product_off, product_valid_images=product_valid_images.split(), product_news=news, product_price_change_type='down', product_color=product_color )
						

				#If There is No Price Change - We Continue With Price Checks 
				elif old_item_current_price == new_item_current_price:
					#This Check is neccesary as most of the items will pass this test
					#No Change in Price, We Do Nothing to Database
					continue

				#If the price is not equal - There is a Hike in Price
				#We Register this also
				elif old_item_current_price < new_item_current_price:
					#If we get here, it means there is an increment in price
					#We reflect that in the News Table Also
					news = product_name + ' price has increased from ' + str(old_item_current_price) + ' to ' + str(new_item_current_price)

					news_item = News.objects.filter(product_url=product_url).count()

					#print('News Item is', news_item)

					if news_item == 1:
						#Update News Object
						
						news_item.update( product_old_price=old_item_current_price, product_current_price=new_item_current_price, product_categories=product_categories.split(','), product_news=news, product_price_change_type='up', product_valid_images=product_valid_images.split() )
						#news_item.update( product_name=product_name, product_seller=product_seller, product_old_price=old_item_current_price, product_current_price=new_item_current_price, product_url=product_url, product_categories=product_categories.split(','), product_news=news, product_price_change_type='up', product_valid_images=product_valid_images.split() )
						
						#We Also Update Product Database for the same entry
						product_item = Product.objects.filter(product_url=product_url)
						product_item.update(  product_old_price=old_item_current_price, product_current_price=new_item_current_price, product_categories=product_categories.split(','), product_valid_images=product_valid_images.split() )
						#product_item.update( product_name=product_name, product_seller=product_seller, product_old_price=old_item_current_price, product_current_price=new_item_current_price, product_url=product_url, product_categories=product_categories.split(',') )
	
					else:
						#We Create New Entry in the News Table
						news_item = News( product_name=product_name, product_seller=product_seller, product_old_price=old_item_current_price, product_current_price=new_item_current_price, product_url=product_url, product_categories=product_categories.split(','), product_valid_sizes=product_valid_sizes.split(), product_off=product_off, product_valid_images=product_valid_images.split(), product_news=news, product_price_change_type='up', product_color=product_color )
						news_item.save()
						#print('Added a New Item that was in Product Table but was not in News Table - Price Up')
						#news_item = News( product_old_price=old_item_current_price, product_current_price=new_item_current_price, product_categories=product_categories.split(','), product_valid_sizes=product_valid_sizes.split(), product_off=product_off, product_valid_images=product_valid_images.split(), product_news=news, product_price_change_type='up', product_color=product_color )
						#print('Created New Up')

				"""
				END OF CHECK IF THERE IS ANY CHANGE IN PRICE FOR EXISTING PRODUCTS
				END OF CHECK IF THERE IS ANY CHANGE IN PRICE FOR EXISTING PRODUCTS
				END OF CHECK IF THERE IS ANY CHANGE IN PRICE FOR EXISTING PRODUCTS
				"""
				##################################################################################################
				##################################################################################################
				##################################################################################################
				##################################################################################################

				

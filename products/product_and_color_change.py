				


				"""
				CHECK IF THERE IS ANY CHANGE IN COLOR CHECK FOR EXISTING PRODUCTS BEGINS
				CHECK IF THERE IS ANY CHANGE IN COLOR CHECK FOR EXISTING PRODUCTS BEGINS
				CHECK IF THERE IS ANY CHANGE IN COLOR CHECK FOR EXISTING PRODUCTS BEGINS
				"""
				#Grab Old Color
				
				old_product_color = arr_item[-1]


				#Compare Old and New Color
				if sorted(old_product_color) == sorted(product_color):
					print( 'THE SAME - Old Product Color = ', old_product_color , 'New Product Color = ', product_color )
					continue
				else:
					print( 'NOT THE SAME - Old Product Color = ', old_product_color , 'New Product Color = ', product_color )
					#If the incoming color is not same with color already in Product DB
					#We have to grab and edit the Color in Both Product and News Table

					#This Check is to know if the Product is also in News Table or Not -- Cos we are currently comparing from Product Table
					news_item = News.objects.filter(product_url=product_url)

					#If it exists there
					if news_item:
						print('Old Product Color is not the same - Step 2')
						#Update that existing entry and that of the Product Table

						news_item.update(product_categories=product_categories.split(','), product_valid_images=product_valid_images.split(), product_color=product_color, product_color_change="Yes" ) 
						#news_item.update( product_name=product_name, product_seller=product_seller, product_url=product_url, product_categories=product_categories.split(','), product_valid_images=product_valid_images.split(), product_color=product_color, product_color_change="Yes" ) 
						#print('Updated Down')
						#We Also Update Product Database for the same entry
						product_item = Product.objects.filter(product_url=product_url)
						product_item.update(product_categories=product_categories.split(','), product_valid_images=product_valid_images.split(), product_color=product_color )
						#product_item.update( product_name=product_name, product_seller=product_seller, product_url=product_url, product_categories=product_categories.split(','), product_valid_images=product_valid_images.split(), product_color=product_color )
					else:
						#This New Change in color is not present in the News Table so we add this Entry
						news_item = News(product_name=product_name, product_seller=product_seller, product_url=product_url, product_categories=product_categories.split(','), product_valid_images=product_valid_images.split(), product_color=product_color, product_color_change="Yes" )
						#news_item = News( product_name=product_name, product_seller=product_seller, product_url=product_url, product_categories=product_categories.split(','), product_valid_images=product_valid_images.split(), product_color=product_color, product_color_change="Yes" )
						news_item.save()

				"""
				END OF CHECK IF THERE IS ANY CHANGE IN COLOR CHECK FOR EXISTING PRODUCTS
				END OF CHECK IF THERE IS ANY CHANGE IN COLOR CHECK FOR EXISTING PRODUCTS
				END OF CHECK IF THERE IS ANY CHANGE IN COLOR CHECK FOR EXISTING PRODUCTS
				"""
				##################################################################################################
				##################################################################################################
				##################################################################################################
				##################################################################################################






















				"""
				CHECK IF THERE IS ANY CHANGE IN SIZE CHECK FOR EXISTING PRODUCTS
				CHECK IF THERE IS ANY CHANGE IN SIZE CHECK FOR EXISTING PRODUCTS
				CHECK IF THERE IS ANY CHANGE IN SIZE CHECK FOR EXISTING PRODUCTS
				"""
				#Grab Old size
				old_product_size = arr_item[6]

				#Compare Old and New size
				if sorted(old_product_size) == sorted(product_valid_sizes):
					print( 'THE SAME - Old Product Size = ', old_product_size , 'New Product Size = ', product_valid_sizes )
					continue
				else:
					print( 'NOT THE SAME - Old Product Size = ', old_product_size , 'New Product Size = ', product_valid_sizes )
					#If the incoming Size is not same with Size already in Product DB
					#We have to grab and edit the Size in Both Product and News Table

					#This Check is to know if the Product is also in News Table or Not -- Cos we are currently comparing from Product Table
					news_item = News.objects.filter(product_url=product_url)

					#If it exists there
					if news_item:
						#Update that existing entry and that of the Product Table

						news_item.update( product_categories=product_categories.split(','), product_valid_sizes=product_valid_sizes.split(), product_valid_images=product_valid_images.split(), product_size_change="Yes" ) 
						#news_item.update( product_name=product_name, product_seller=product_seller, product_url=product_url, product_categories=product_categories.split(','), product_valid_sizes=product_valid_sizes.split(), product_valid_images=product_valid_images.split(), product_size_change="Yes" ) 
						#print('Updated Down')
						#We Also Update Product Database for the same entry
						product_item = Product.objects.filter(product_url=product_url)
						product_item.update( product_categories=product_categories.split(','), product_valid_sizes=product_valid_sizes.split(), product_valid_images=product_valid_images.split() )
						#product_item.update( product_name=product_name, product_seller=product_seller, product_url=product_url, product_categories=product_categories.split(','), product_valid_sizes=product_valid_sizes.split(), product_valid_images=product_valid_images.split() )
					else:
						#This New Change in size is not present in the News Table so we add this Entry
						news_item = News( product_name=product_name, product_seller=product_seller, product_url=product_url, product_categories=product_categories.split(','), product_valid_sizes=product_valid_sizes.split(), product_valid_images=product_valid_images.split(), product_size_change="Yes" )
						#news_item = News( product_name=product_name, product_seller=product_seller, product_url=product_url, product_categories=product_categories.split(','), product_valid_sizes=product_valid_sizes.split(), product_valid_images=product_valid_images.split(), product_size_change="Yes" )
						news_item.save()
				"""
				END OF SIZES CHECK IF THERE IS ANY CHANGE IN SIZE CHECK FOR EXISTING PRODUCTS
				END OF SIZES CHECK IF THERE IS ANY CHANGE IN SIZE CHECK FOR EXISTING PRODUCTS
				END OF SIZES CHECK IF THERE IS ANY CHANGE IN SIZE CHECK FOR EXISTING PRODUCTS
				"""

































				"""
				CHECK IF THERE IS ANY CHANGE IN COLOR CHECK FOR EXISTING PRODUCTS BEGINS
				CHECK IF THERE IS ANY CHANGE IN COLOR CHECK FOR EXISTING PRODUCTS BEGINS
				CHECK IF THERE IS ANY CHANGE IN COLOR CHECK FOR EXISTING PRODUCTS BEGINS
				"""
				#Grab Old Color
				
				old_product_color = arr_item[-1]


				#Convert Color Types to String for Easy Comparison
				old_color_type = type(old_product_color)
				new_color_type = type(product_color)

				if old_color_type == list:
					str_old_product_color = ' '.join(old_product_color)
				else:
					str_old_product_color = old_product_color

				
				if new_color_type == list:
					str_product_color = ' '.join(product_color)
				else:
					str_product_color = product_color


				#Compare Old and New Color
				if str_old_product_color != str_product_color:

					print( 'NOT THE SAME - Old Product Color = ', str_old_product_color , 'is not Equal to New Product Color = ', str_product_color )
					#If the incoming color is not same with color already in Product DB
					#We have to grab and edit the Color in Both Product and News Table

					
					#This Check is to know if the Product is also in News Table or Not -- Cos we are currently comparing from Product Table
					news_item = News.objects.filter(product_url=product_url)
					print("News Item", news_item)


					#If it exists there
					if news_item:
						
						print('There is an existing product so we update')
						#Update that existing entry and that of the Product Table

						news_item.update(product_categories=product_categories.split(','), product_valid_images=product_valid_images.split(), product_color=product_color, product_color_change="Yes" ) 
						#news_item.update( product_name=product_name, product_seller=product_seller, product_url=product_url, product_categories=product_categories.split(','), product_valid_images=product_valid_images.split(), product_color=product_color, product_color_change="Yes" ) 
						#print('Updated Down')
						
						#We Also Update Product Database for the same entry
						product_item = Product.objects.filter(product_url=product_url)
						product_item.update(product_categories=product_categories.split(','), product_valid_images=product_valid_images.split(), product_color=product_color )
						#product_item.update( product_name=product_name, product_seller=product_seller, product_url=product_url, product_categories=product_categories.split(','), product_valid_images=product_valid_images.split(), product_color=product_color )
					else:
						#This New Change in color is not present in the News Table so we add this Entry
						news_item = News(product_name=product_name, product_seller=product_seller, product_url=product_url, product_categories=product_categories.split(','), product_valid_images=product_valid_images.split(), product_color=product_color, product_color_change="Yes" )
						#news_item = News( product_name=product_name, product_seller=product_seller, product_url=product_url, product_categories=product_categories.split(','), product_valid_images=product_valid_images.split(), product_color=product_color, product_color_change="Yes" )
						news_item.save()

				"""
				END OF CHECK IF THERE IS ANY CHANGE IN COLOR CHECK FOR EXISTING PRODUCTS
				END OF CHECK IF THERE IS ANY CHANGE IN COLOR CHECK FOR EXISTING PRODUCTS
				END OF CHECK IF THERE IS ANY CHANGE IN COLOR CHECK FOR EXISTING PRODUCTS
				"""
				##################################################################################################
				##################################################################################################
				##################################################################################################
				##################################################################################################
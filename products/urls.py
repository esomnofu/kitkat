from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
   
    #path('products/', views.products, name='products'),
    path('crawl/', views.crawl, name='crawl'),

    #path('products/', views.products, name='products'),
    path('train/', views.train, name='train'),

    #Form View
    path('form/', views.form, name='form'),
    #path('detail/<int:id>/', views.detail, name='detail'),
        
    #Search Query
    path('search/', views.search, name='search'),

    #NewsFeed Query
    path('newsfeed/', views.newsfeed, name='newsfeed'),

    #Increment In Price Query
    path('increase/', views.increase, name='increase'),

    #Reduction in Price Query
    path('reduce/', views.reduce, name='reduce'),

    #Change in Colors Query
    path('color/', views.color, name='color'),

    #Change in Size Query
    path('size/', views.size, name='size'),



    #ITEM BASED RECOMMENDATIONS URLS
    #ITEM BASED RECOMMENDATIONS URLS
    #ITEM BASED RECOMMENDATIONS URLS
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.loggedout, name='logout'),
    path('newsroom/', views.newsroom, name='newsroom'),
    path('create/', views.create, name='create'),
    path('recommend/', views.recommend, name='recommend')



]

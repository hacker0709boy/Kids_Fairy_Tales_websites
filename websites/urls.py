from django.urls import path 

from . import views


urlpatterns = [
	path('', views.index, name= "index"),
    path('indextm', views.indextm, name= "indextm"),
    path('about/', views.about, name= "about"),
    path('abouttm/', views.abouttm, name= "abouttm"),
    path('contact/', views.contact, name= "contact"),
    path('contacttm/', views.contacttm, name= "contacttm"),
    path('work/', views.work, name= "work"),
    path('worktm/', views.worktm, name= "worktm"),
    path('snow/', views.snow, name= "snow"),


    path('send_email/', views.contact, name='send_email'),
    
]
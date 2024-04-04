from django.urls import path
from core import views

urlpatterns = [  
    #path('', views.home, name = 'home'), 
    path('index/', views.index , name = 'index'),
    path('about/', views.about , name = 'about'),
    path('program/', views.program , name = 'program'),
    path('contact/', views.contact , name = 'contact'),
    path('base1/', views.base1 , name = 'base1'),
    path('programdetail/', views.programdetail , name = 'pd'),
    
    
]


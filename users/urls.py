from django.urls import path 
from .views import user_create,user_details

urlpatterns =[
    path("users/",user_create),
    path("users/<int:user_id>/",user_details),
   
    
]
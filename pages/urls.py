
from django.urls import path
from pages.views import home, contact, about

urlpatterns = [
    path('', home),
    
    path('mypage', mypage),   
    path('contact/', contact),
    path('about/', about),
]

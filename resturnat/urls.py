from django.urls import path
from.views import Home,Qoutes,Book,home,Menu,About

urlpatterns = [
    path('',home,name='home' ),
    path('quotes/',Qoutes.as_view(),name='quotes'),
    path('book/',Book.as_view(),name='book'),
    path('menu/',Menu.as_view(),name='menu'),
    path('about/',About.as_view(),name='about'),
   

    
]

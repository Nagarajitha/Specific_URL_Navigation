from django.urls import path
from drinks.views import *
app_name ='drinks'
urlpatterns =[ 
    path('dewars/',dewars,name='dewars'),
    path('teachers/',teachers,name='teachers'),
]
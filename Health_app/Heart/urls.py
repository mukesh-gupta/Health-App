from django.urls import path
from . import views

urlpatterns = [
    path('',views.Heart,name='heart'),
path('result/',views.result,name='heartresult')
    ]
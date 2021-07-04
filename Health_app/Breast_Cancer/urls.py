from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name='home'),
    path('cancer/',views.Cancer,name='cancer'),
path('result/',views.result,name='result')
    ]
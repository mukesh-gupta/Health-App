from django.urls import path
from . import views

urlpatterns = [
#path('',views.home,name='home'),
    path('',views.Diabetes,name='diabetes'),
path('result/',views.result,name='diabresult')
    ]

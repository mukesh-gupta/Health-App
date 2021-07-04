from django.urls import path
from . import views

urlpatterns = [
    path('',views.Kidney,name='kidney'),
path('result/',views.result,name='kidresult')
    ]
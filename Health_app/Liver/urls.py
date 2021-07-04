from django.urls import path
from . import views

urlpatterns = [
    path('',views.Liver,name='liver'),
path('result/',views.result,name='liverresult')
    ]

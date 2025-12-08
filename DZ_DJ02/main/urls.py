from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('page2', views.page2, name='second'),
    path('page3', views.page3, name='third'),
    path('page4', views.page4, name='fourth')
]
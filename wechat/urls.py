from django.urls import path
from . import views

app_name = 'wechat'

urlpatterns = [
    path('', views.handle, name='handle'),
    ]

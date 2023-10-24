from django.urls import path
from .import views

from .views import *

urlpatterns = [
    path('', developer_home_page, name='developer_home'),
]
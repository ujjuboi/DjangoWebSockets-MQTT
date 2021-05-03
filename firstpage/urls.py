from django.urls import path
from firstpage.views import Firstpage
from django.conf.urls import url
from .views import (
    login_view, register_view,
)

urlpatterns = [
    path('', Firstpage, name = 'firstPage'),
    url(r"^login/$", login_view, name = "login"), 
    url(r"^register/$", register_view, name = "register"), 
]
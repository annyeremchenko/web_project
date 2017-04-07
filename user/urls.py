from django.conf.urls import url, include
from django.contrib import admin
import user
from . import views
urlpatterns = [
    url(r'signin/', views.Signin.as_view(), name='sign in'),  # вхід
    url(r'signout/', views.Signout.as_view(), name='sign out'),  # вихід
    url(r'signup/', views.Signup.as_view(), name='sign up'),  # реєстрація
]
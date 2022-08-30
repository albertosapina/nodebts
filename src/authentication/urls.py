from django.contrib import admin
from django.urls import path

from .views import CreateToken

#auth
urlpatterns = [
    path('token/', CreateToken.as_view()),
]
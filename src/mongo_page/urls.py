from django.contrib import admin
from django.urls import path
from .views import MongoPage, MongoPageDetail

# mongopage/
urlpatterns = [
    path('', MongoPage.as_view()),
    path('<str:id>/', MongoPageDetail.as_view())
]
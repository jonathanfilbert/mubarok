from django.urls import path
from . import views

urlpatterns = [
    path('get-story/',views.api)
]
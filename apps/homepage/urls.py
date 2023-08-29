from django.urls import path
from .views import *

app_name = "homepage"

urlpatterns = [
    path("home/", HomePageView.as_view(), name="home"),
]

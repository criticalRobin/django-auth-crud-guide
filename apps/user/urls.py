from django.urls import path
from .views import UserCreateView


app_name = "user"

urlpatterns = [
    path("create/", UserCreateView.as_view(), name="user_create"),
]

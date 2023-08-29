from django.urls import path
from .views import *

app_name = "login"

urlpatterns = [
    path("", LoginFormView.as_view(), name="login_view"),
    path("logout/", LogoutFormView.as_view(), name="logout_view"),
]

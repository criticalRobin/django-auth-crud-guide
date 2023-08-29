from django import forms
from django.template.defaultfilters import capfirst
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = capfirst(form.name)
        self.fields["username"].widget.attrs["autofocus"] = True

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        labels = {
            "username": "Username",
            "password1": "Password",
            "password2": "Confirm Password",
        }

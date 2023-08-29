from django.forms import ModelForm
from apps.main.models import *


class AuthorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = "Ingresar " + form.label.lower()
        self.fields["first_name"].widget.attrs["autofocus"] = True

    class Meta:
        model = Author
        fields = "__all__"
        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido",
            "nationality": "Nacionalidad",
            "age": "Edad",
        }


class PublisherForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = "Ingresar " + form.label.lower()
        self.fields["name"].widget.attrs["autofocus"] = True

    class Meta:
        model = Publisher
        fields = "__all__"
        labels = {
            "name": "Nombre",
            "location": "Ubicacion",
        }


class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = "Ingresar " + form.label.lower()
        self.fields["name"].widget.attrs["autofocus"] = True
        self.fields["publish_date"].widget.attrs["placeholder"] = "YYYY-MM-DD"

    class Meta:
        model = Book
        fields = "__all__"
        labels = {
            "name": "Nombre",
            "author": "Autor",
            "publish_date": "Fecha de Publicacion",
            "pages": "Paginas",
            "publisher": "Editorial",
            "price": "Precio",
        }

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .validations import Validations

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(
        max_length=50, validators=[Validations.validate_char_fields]
    )
    last_name = models.CharField(
        max_length=50, validators=[Validations.validate_char_fields]
    )
    nationality = models.CharField(
        max_length=100, validators=[Validations.validate_char_fields]
    )
    age = models.IntegerField(
        default=18, validators=[MaxValueValidator(100), MinValueValidator(18)]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    name = models.CharField(
        max_length=100, unique=True, validators=[Validations.validate_char_fields]
    )
    location = models.CharField(
        max_length=100, validators=[Validations.validate_char_fields]
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(
        max_length=100, unique=True, validators=[Validations.validate_char_fields]
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateField(auto_now=False, auto_now_add=False)
    pages = models.IntegerField(validators=[MinValueValidator(30)])
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0.00)],
    )

    def __str__(self):
        return self.name

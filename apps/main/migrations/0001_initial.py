# Generated by Django 4.2.4 on 2023-08-23 02:03

import apps.main.validations
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, validators=[apps.main.validations.Validations.validate_char_fields])),
                ('last_name', models.CharField(max_length=50, validators=[apps.main.validations.Validations.validate_char_fields])),
                ('nationality', models.CharField(max_length=100, validators=[apps.main.validations.Validations.validate_char_fields])),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[apps.main.validations.Validations.validate_char_fields])),
                ('location', models.CharField(max_length=100, validators=[apps.main.validations.Validations.validate_char_fields])),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[apps.main.validations.Validations.validate_char_fields])),
                ('publish_date', models.DateField()),
                ('pages', models.IntegerField(validators=[django.core.validators.MinValueValidator(30)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.publisher')),
            ],
        ),
    ]

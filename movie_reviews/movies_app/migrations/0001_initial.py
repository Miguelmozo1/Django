# Generated by Django 5.0.4 on 2024-05-25 21:07

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('review', models.CharField(max_length=355)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='users_app.user')),
                ('reviews', models.ManyToManyField(related_name='reviews', to='users_app.user')),
            ],
        ),
    ]

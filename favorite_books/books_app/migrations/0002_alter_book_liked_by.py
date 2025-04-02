# Generated by Django 5.0.4 on 2024-05-20 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0001_initial'),
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='liked_by',
            field=models.ManyToManyField(related_name='favorites', to='users_app.user'),
        ),
    ]

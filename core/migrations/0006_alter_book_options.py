# Generated by Django 4.0.3 on 2022-03-21 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_authorprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['pages'], 'verbose_name': 'Книги', 'verbose_name_plural': 'Книги'},
        ),
    ]
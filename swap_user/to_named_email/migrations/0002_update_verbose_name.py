# Generated by Django 2.2.16 on 2020-11-12 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("swap_to_named_email", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="namedemailuser",
            options={"verbose_name": "email user", "verbose_name_plural": "email users"},
        ),
    ]

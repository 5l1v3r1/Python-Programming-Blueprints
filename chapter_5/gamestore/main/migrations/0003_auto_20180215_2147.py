# Generated by Django 2.0.1 on 2018-02-15 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_pricelist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='imagelink',
            new_name='image',
        ),
    ]

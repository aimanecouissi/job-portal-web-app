# Generated by Django 4.0.4 on 2022-05-04 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruteur', '0010_alter_offre_rec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offre',
            name='rec',
        ),
    ]

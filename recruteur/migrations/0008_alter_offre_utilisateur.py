# Generated by Django 4.0.4 on 2022-05-04 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruteur', '0007_alter_offre_utilisateur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='utilisateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

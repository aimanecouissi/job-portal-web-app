# Generated by Django 4.0.4 on 2022-05-22 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demandeur', '0005_alter_demande_options_cv_cin_cv_sexe'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='civi',
            field=models.FileField(null=True, upload_to='cv/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='cv',
            name='lettre',
            field=models.FileField(null=True, upload_to='lettres/%Y/%m/%d/'),
        ),
    ]

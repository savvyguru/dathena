# Generated by Django 3.0.9 on 2020-08-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20200805_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_meta',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-29 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentapp',
            name='inter_memo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentapp',
            name='ssc_memo',
            field=models.IntegerField(),
        ),
    ]

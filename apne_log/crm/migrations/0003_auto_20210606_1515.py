# Generated by Django 3.2.4 on 2021-06-06 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_rename_user_details_certificate_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate_details',
            name='end',
            field=models.CharField(max_length=245),
        ),
        migrations.AlterField(
            model_name='certificate_details',
            name='start',
            field=models.CharField(max_length=245),
        ),
    ]
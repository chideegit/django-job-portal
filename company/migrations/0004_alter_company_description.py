# Generated by Django 5.0.3 on 2024-03-08 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_company_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

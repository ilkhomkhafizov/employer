# Generated by Django 4.1.2 on 2022-10-21 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_remove_employee_level_remove_employee_lft_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employment_start_date',
            field=models.DateField(),
        ),
    ]

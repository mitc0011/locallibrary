# Generated by Django 2.1.5 on 2022-06-03 10:43

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_auto_20220603_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_file',
            field=models.FileField(blank=True, null=True, upload_to=catalog.models.Book.book_file_name),
        ),
    ]

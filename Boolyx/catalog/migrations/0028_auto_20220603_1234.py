# Generated by Django 2.1.5 on 2022-06-03 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0027_auto_20220603_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_file',
            field=models.FileField(blank=True, null=True, upload_to=models.CharField(max_length=200)),
        ),
    ]
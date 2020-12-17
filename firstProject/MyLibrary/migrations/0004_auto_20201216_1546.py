# Generated by Django 3.1.3 on 2020-12-16 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyLibrary', '0003_auto_20201216_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

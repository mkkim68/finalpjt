# Generated by Django 4.2.4 on 2024-05-17 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='max_limit',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='mtrt_int',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='saving',
            name='max_limit',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='saving',
            name='mtrt_int',
            field=models.TextField(),
        ),
    ]

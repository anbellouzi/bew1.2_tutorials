# Generated by Django 2.2.6 on 2019-10-25 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_pizza_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='price',
            field=models.CharField(default='Pesto', max_length=200),
            preserve_default=False,
        ),
    ]
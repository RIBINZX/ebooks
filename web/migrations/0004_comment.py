# Generated by Django 4.1.7 on 2023-05-22 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]

# Generated by Django 3.2 on 2024-12-06 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20241201_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cashinhand', models.IntegerField(blank=True, null=True)),
                ('cashatbank', models.IntegerField(blank=True, null=True)),
                ('cashatbankexp', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

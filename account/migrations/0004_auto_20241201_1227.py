# Generated by Django 3.2 on 2024-12-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_expense_id_alter_expensetype_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='expid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='incid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

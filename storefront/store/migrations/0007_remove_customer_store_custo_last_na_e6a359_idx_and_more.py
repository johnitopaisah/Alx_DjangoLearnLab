# Generated by Django 5.1 on 2024-08-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_customer_membership_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='customer',
            name='store_custo_last_na_e6a359_idx',
        ),
        migrations.AlterField(
            model_name='customer',
            name='membership',
            field=models.CharField(choices=[('S', 'Sylver'), ('G', 'Gold'), ('B', 'Bronze')], default='B', max_length=1),
        ),
        migrations.AlterModelTable(
            name='customer',
            table=None,
        ),
    ]

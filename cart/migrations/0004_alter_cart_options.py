# Generated by Django 5.0.6 on 2024-07-02 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cart_session_key_alter_cart_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
    ]

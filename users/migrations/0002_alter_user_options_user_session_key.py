# Generated by Django 5.0.6 on 2024-07-02 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='user',
            name='session_key',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='Временная регистрация'),
        ),
    ]

# Generated by Django 4.1.1 on 2022-11-14 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveIntegerField(verbose_name='Зовнішній Id')),
                ('name', models.CharField(max_length=128, verbose_name='Імя користувача')),
            ],
            options={
                'verbose_name': 'Профіль',
                'verbose_name_plural': 'Профілі',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата отримання')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='telegram.profile', verbose_name='Профіль')),
            ],
            options={
                'verbose_name': 'Півідомлення',
                'verbose_name_plural': 'Повідомлення',
            },
        ),
    ]

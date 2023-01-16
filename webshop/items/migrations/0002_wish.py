# Generated by Django 4.0.6 on 2022-08-03 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='текст бегущей строки')),
                ('date', models.DateTimeField(verbose_name='дата запроса')),
            ],
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

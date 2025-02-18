# Generated by Django 5.1.1 on 2024-10-23 04:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_userproduct_productuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_code', models.CharField(max_length=100, unique=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cours')),
            ],
        ),
        migrations.DeleteModel(
            name='book',
        ),
        migrations.DeleteModel(
            name='customer1model',
        ),
        migrations.DeleteModel(
            name='employee',
        ),
        migrations.DeleteModel(
            name='product',
        ),
        migrations.RemoveField(
            model_name='productuser',
            name='user_p',
        ),
        migrations.DeleteModel(
            name='user',
        ),
        migrations.DeleteModel(
            name='productuser',
        ),
        migrations.DeleteModel(
            name='userproduct',
        ),
    ]

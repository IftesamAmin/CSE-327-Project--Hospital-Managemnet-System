# Generated by Django 3.2.1 on 2021-05-06 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('phone', models.IntegerField()),
                ('status', models.CharField(default='register', max_length=50)),
            ],
        ),
    ]

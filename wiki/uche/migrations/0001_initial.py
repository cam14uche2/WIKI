# Generated by Django 4.0.6 on 2022-07-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='UserName')),
                ('last_name', models.CharField(max_length=200, verbose_name='UserName')),
                ('phone', models.CharField(max_length=17, verbose_name='contact phone')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email Address')),
            ],
        ),
    ]

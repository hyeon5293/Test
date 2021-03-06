# Generated by Django 3.2.6 on 2021-08-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('furniture_Name', models.CharField(max_length=100)),
                ('furniture_Link', models.URLField()),
                ('sale_Percentage', models.CharField(max_length=10)),
                ('current_Price', models.CharField(max_length=20)),
                ('previous_Price', models.CharField(max_length=20)),
                ('furniture_Img', models.URLField()),
            ],
        ),
    ]

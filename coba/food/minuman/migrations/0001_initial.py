# Generated by Django 3.2.8 on 2021-10-15 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='minuman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=255)),
                ('nama', models.CharField(max_length=255)),
                ('harga', models.IntegerField()),
            ],
        ),
    ]

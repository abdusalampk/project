# Generated by Django 4.2.1 on 2023-06-10 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('place', models.TextField()),
                ('img', models.ImageField(upload_to='ooty derox')),
            ],
        ),
    ]

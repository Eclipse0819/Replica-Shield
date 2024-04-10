# Generated by Django 5.0.4 on 2024-04-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('leader', models.CharField(max_length=50)),
                ('leader_email', models.EmailField(max_length=254)),
                ('member2', models.CharField(max_length=50)),
                ('member3', models.CharField(blank=True, max_length=50)),
                ('member4', models.CharField(blank=True, max_length=50)),
                ('abstract', models.TextField()),
            ],
        ),
    ]
# Generated by Django 5.1.4 on 2025-03-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Computer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='C_Acer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField()),
                ('image', models.URLField(blank=True, null=True)),
                ('price', models.FloatField(null=True)),
                ('date_post', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

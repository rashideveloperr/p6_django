# Generated by Django 4.1.3 on 2022-11-17 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0008_blog_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]

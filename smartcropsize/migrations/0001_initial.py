# Generated by Django 3.0.4 on 2021-07-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmartcropImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=256, null=True, upload_to='uploads/')),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
        ),
    ]

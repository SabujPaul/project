# Generated by Django 4.1.7 on 2023-03-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autistic', '0002_alter_predresults_birth_injury_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
            ],
        ),
    ]

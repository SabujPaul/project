# Generated by Django 4.1.7 on 2023-03-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresults',
            name='Birth_Injury',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Cousin_Marriage',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Delivery',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Gender',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Jaundice',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Q1',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Q10',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Q11',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Q2',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Q3',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Q4',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Q5',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Q6',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Q7',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Q8',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Q9',
            field=models.CharField(max_length=30),
        ),
    ]

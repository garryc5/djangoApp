# Generated by Django 2.2.3 on 2019-09-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(choices=[('R', 'Running'), ('A', 'Arms'), ('L', 'Legs'), ('C', 'Core')], default='R', max_length=1)),
                ('weight', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Calories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories_in', models.IntegerField()),
                ('calories_out', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(verbose_name='date of birth')),
                ('picture', models.CharField(max_length=100)),
                ('sport_bio', models.TextField(max_length=250)),
                ('goal', models.CharField(max_length=150)),
            ],
        ),
    ]

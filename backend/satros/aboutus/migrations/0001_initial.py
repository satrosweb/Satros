# Generated by Django 4.2.7 on 2023-11-16 18:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=200, unique=True, verbose_name='جایگاه')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'دسته بندی جایگاه',
                'verbose_name_plural': 'دسته بندی جایگاه ها',
                'ordering': ['-job'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=200, verbose_name='مهارت')),
                ('mastery_persent', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='درصد تسلط')),
            ],
            options={
                'verbose_name': 'مهارت',
                'verbose_name_plural': 'مهارت ها',
                'ordering': ['skill'],
            },
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='نام')),
                ('position', models.CharField(choices=[('SN', 'Senior'), ('JN', 'Junior')], max_length=2, verbose_name='جایگاه')),
                ('image', models.ImageField(upload_to='aboutus/employees/image/', verbose_name='تصویر')),
                ('resume_summery', models.TextField(verbose_name='خلاصه ی رزومه')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employe_position', to='aboutus.mainjob', verbose_name='شغل')),
                ('skills', models.ManyToManyField(blank=True, to='aboutus.skill', verbose_name='مهارت ها')),
            ],
            options={
                'verbose_name': 'کارمند',
                'verbose_name_plural': 'کارمندان',
                'ordering': ['-position'],
            },
        ),
    ]
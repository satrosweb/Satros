# Generated by Django 4.2.7 on 2023-11-15 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('main_image', models.ImageField(upload_to='projects/image/main_image')),
                ('small_description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('NC', 'NotCompeleted'), ('C', 'Compeleted')], default='NC', max_length=2)),
                ('started', models.DateTimeField()),
                ('ended', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['-name'], name='projects_ca_name_dcbe4d_idx'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['-created'], name='projects_pr_created_5ace3f_idx'),
        ),
    ]

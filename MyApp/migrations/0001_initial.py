# Generated by Django 5.1.1 on 2024-09-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student', models.CharField(blank=True, max_length=100, null=True)),
                ('Batch', models.CharField(blank=True, max_length=100, null=True)),
                ('Tutor', models.CharField(blank=True, max_length=100, null=True)),
                ('Task', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]

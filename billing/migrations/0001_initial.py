# Generated by Django 5.1.3 on 2024-11-10 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=20)),
                ('emp_no', models.IntegerField()),
                ('emp_design', models.CharField(max_length=20)),
                ('mob_no', models.IntegerField()),
            ],
        ),
    ]

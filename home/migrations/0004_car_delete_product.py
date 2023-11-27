# Generated by Django 4.2.7 on 2023-11-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_student_file_remove_student_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('speed', models.IntegerField(default=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]

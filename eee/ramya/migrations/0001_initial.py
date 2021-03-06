# Generated by Django 4.0.2 on 2022-02-28 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('password', models.IntegerField()),
                ('repassword', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to='')),
                ('file', models.FileField(upload_to='')),
                ('gender', models.CharField(choices=[['MALE', 'MALE'], ['FEMALE', 'FEMALE']], max_length=10)),
                ('dob', models.DateField()),
            ],
        ),
    ]

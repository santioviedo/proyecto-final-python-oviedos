# Generated by Django 4.2.8 on 2024-01-23 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appcasino', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='premios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cajeron', models.CharField(max_length=25)),
                ('nombreu', models.CharField(max_length=25)),
                ('importe', models.IntegerField()),
                ('cvu', models.IntegerField()),
            ],
        ),
    ]
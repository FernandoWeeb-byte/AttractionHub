# Generated by Django 3.2.9 on 2021-12-03 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('title', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='attraction',
            name='stream',
            field=models.ManyToManyField(to='listManager.Stream'),
        ),
    ]

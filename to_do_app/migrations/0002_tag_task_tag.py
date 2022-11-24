# Generated by Django 4.0.4 on 2022-11-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='tag',
            field=models.ManyToManyField(to='to_do_app.tag'),
        ),
    ]
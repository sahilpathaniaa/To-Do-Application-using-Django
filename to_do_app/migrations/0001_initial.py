# Generated by Django 4.0.4 on 2022-11-22 20:02

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
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('dueDate', models.DateField(blank=True)),
                ('status', models.CharField(choices=[('open', 'OPEN'), ('working', 'WORKING'), ('done', 'DONE'), ('overdue', 'OVERDUE')], default='open', max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
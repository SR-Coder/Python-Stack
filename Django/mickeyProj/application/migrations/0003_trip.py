# Generated by Django 2.2.4 on 2021-03-19 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='application.User')),
                ('users_joined', models.ManyToManyField(related_name='trips_joined', to='application.User')),
            ],
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-04 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0002_to_do'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('allergens', models.CharField(max_length=50)),
                ('guestlist', models.ManyToManyField(to='registry.guestlist')),
            ],
        ),
    ]
# Generated by Django 4.2.1 on 2023-06-16 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salarie',
            fields=[
                ('id_salarie', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('email_professional', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'salarie',
                'managed': False,
            },
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-04 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test1',
            fields=[
                ('Keyword', models.TextField(blank=True, db_column='Keyword', primary_key=True, serialize=False)),
                ('count', models.BigIntegerField(blank=True, db_column='count', null=True)),
            ],
            options={
                'db_table': None,
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-16 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0018_remove_basicinfo_candidateid_basicinfo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
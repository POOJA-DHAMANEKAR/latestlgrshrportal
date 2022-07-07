# Generated by Django 4.0.4 on 2022-07-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0031_basicinfo_client_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicinfo',
            name='current_job_location',
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='call_or_interview_remarks',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='client_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='current_location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='designated_as',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='exp_ctc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='interview_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='interviewed_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='notice_period',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='ready_to_relocate',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='resume_received_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='total_experience',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

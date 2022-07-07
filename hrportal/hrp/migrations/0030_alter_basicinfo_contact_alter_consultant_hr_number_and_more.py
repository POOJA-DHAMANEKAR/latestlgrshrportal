# Generated by Django 4.0.4 on 2022-06-28 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0029_basicinfo_applied_for_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='contact',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='HR_number',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=50, null=True)),
                ('university_name', models.CharField(blank=True, max_length=300, null=True)),
                ('percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('year_of_passing', models.IntegerField(blank=True, null=True)),
                ('basic_education', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basic_education', to='hrp.basicinfo')),
            ],
        ),
    ]
# Generated by Django 3.0.5 on 2020-04-05 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200406_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dp',
            name='Dept_Loc',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Dept Loc'),
        ),
        migrations.AlterField(
            model_name='dp',
            name='PS_NO',
            field=models.FloatField(blank=True, null=True, verbose_name='PS NO'),
        ),
    ]
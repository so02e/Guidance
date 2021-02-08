# Generated by Django 3.1.5 on 2021-02-08 02:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bbsApp', '0003_auto_20210205_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='academy_review',
            name='title',
            field=models.CharField(default='제목없음', max_length=45),
        ),
        migrations.AddField(
            model_name='academy_review',
            name='writedate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testsite_review',
            name='title',
            field=models.CharField(default='제목없음', max_length=45),
        ),
        migrations.AddField(
            model_name='testsite_review',
            name='writedate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-13 20:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home_post',
            options={'ordering': ['-publishing_date']},
        ),
        migrations.AlterModelOptions(
            name='home_static',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='home_post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='home_static',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='içerik'),
        ),
    ]

# Generated by Django 3.2.3 on 2021-08-02 12:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realtext', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]

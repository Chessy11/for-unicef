# Generated by Django 3.1.11 on 2021-05-20 11:02

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210520_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='polls.pollpage'),
        ),
    ]

# Generated by Django 4.0.7 on 2022-10-07 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0076_modellogentry_revision'),
        ('home', '0003_indexpage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IndexPage',
            new_name='PoemPage',
        ),
    ]
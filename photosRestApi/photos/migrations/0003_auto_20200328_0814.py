# Generated by Django 3.0.4 on 2020-03-28 08:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0002_auto_20200328_0808'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photos',
            new_name='Photo',
        ),
    ]
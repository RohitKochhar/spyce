# Generated by Django 3.1.3 on 2020-12-13 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filterdesigner', '0002_rclowpass'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rclowpass',
            old_name='s_CapacitanceInput',
            new_name='f_Capacitance',
        ),
        migrations.RenameField(
            model_name='rclowpass',
            old_name='s_ResistanceInput',
            new_name='f_Resistance',
        ),
    ]

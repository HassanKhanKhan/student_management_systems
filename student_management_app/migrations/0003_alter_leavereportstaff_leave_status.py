# Generated by Django 3.2.7 on 2021-10-07 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0002_alter_attendance_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereportstaff',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
    ]

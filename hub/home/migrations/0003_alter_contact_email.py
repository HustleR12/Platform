# Generated by Django 4.1.2 on 2023-02-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_contact_id_contact_email_contact_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='xyz@gmail.com', max_length=100),
        ),
    ]
# Generated by Django 4.0.2 on 2022-05-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epassqr',
            name='qr_img',
            field=models.ImageField(upload_to='gen/qr_data'),
        ),
    ]
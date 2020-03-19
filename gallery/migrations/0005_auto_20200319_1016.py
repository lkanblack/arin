# Generated by Django 2.2.7 on 2020-03-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20200319_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_title', models.CharField(max_length=200)),
                ('shop_image', models.ImageField(upload_to='gallery/')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='shop_image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='shop_title',
        ),
    ]
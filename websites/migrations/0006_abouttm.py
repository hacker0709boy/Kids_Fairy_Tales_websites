# Generated by Django 4.0 on 2021-12-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0005_rename_aboutus_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abouttm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('sub_headline', models.CharField(blank=True, max_length=200, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='img')),
                ('body', models.TextField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(null=True, to='websites.Tag')),
            ],
        ),
    ]

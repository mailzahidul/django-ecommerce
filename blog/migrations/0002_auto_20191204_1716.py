# Generated by Django 2.2.7 on 2019-12-04 17:16

import blog.models
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BlogCrete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', multiselectfield.db.fields.MultiSelectField(max_length=200, verbose_name=blog.models.BlogCategories)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('feature_img', models.ImageField(upload_to='blogs/%Y/%m/%d')),
                ('blog_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.SignupInfo')),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]

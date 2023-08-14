# Generated by Django 4.2.4 on 2023-08-14 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('descriptions', models.TextField(blank=True, verbose_name='Description')),
                ('avatar', models.ImageField(blank=True, upload_to='categories/', verbose_name='Avatar')),
                ('is_enable', models.BooleanField(default=True, verbose_name='IS enable')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Updated time')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('avatar', models.ImageField(blank=True, upload_to='products/', verbose_name='Avatar')),
                ('is_enable', models.BooleanField(default=True, verbose_name='Is enable')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Updated time')),
                ('categories', models.ManyToManyField(blank=True, to='products.category', verbose_name='categories')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('file', models.FileField(upload_to='files/%y/%m/%d', verbose_name='File')),
                ('is_enable', models.BooleanField(default=True, verbose_name='Is enable')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Updated time')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
                'db_table': 'files',
            },
        ),
    ]
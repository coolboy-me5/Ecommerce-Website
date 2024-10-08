# Generated by Django 5.1.1 on 2024-09-23 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.categories'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(null=True, upload_to='categories/images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='products/images/'),
        ),
    ]

# Generated by Django 2.2.10 on 2020-08-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200807_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='themes',
            field=models.ManyToManyField(related_name='themes', through='articles.ArticleScope', to='articles.Theme'),
        ),
    ]
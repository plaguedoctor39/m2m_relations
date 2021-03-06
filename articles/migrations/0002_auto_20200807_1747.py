# Generated by Django 2.2.10 on 2020-08-07 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название тематики')),
            ],
            options={
                'verbose_name': 'Тематика',
                'verbose_name_plural': 'Тематики',
            },
        ),
        migrations.CreateModel(
            name='ArticleScope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(blank=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Theme')),
            ],
            options={
                'db_table': 'articles and themes',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='themes',
            field=models.ManyToManyField(related_name='articles', through='articles.ArticleScope', to='articles.Theme'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-04 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210929_1314'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posted',
            new_name='Content',
        ),
        migrations.AlterField(
            model_name='influencer',
            name='field',
            field=models.CharField(choices=[('Comedy', 'Comedy'), ('Commentary', 'Commentary'), ('Educational', 'Educational'), ('Fashion', 'Fashion'), ('Food', 'Food'), ('Gaming', 'Gaming'), ('Interview', 'Interview'), ('Music', 'Music'), ('ProductReview', 'ProductReview'), ('Q&A', 'Q&A'), ('Reaction', 'Reaction'), ('Sport', 'Sport'), ('Travel', 'Travel')], max_length=50),
        ),
        migrations.AlterField(
            model_name='influencerpost',
            name='field',
            field=models.CharField(choices=[('Comedy', 'Comedy'), ('Commentary', 'Commentary'), ('Educational', 'Educational'), ('Fashion', 'Fashion'), ('Food', 'Food'), ('Gaming', 'Gaming'), ('Interview', 'Interview'), ('Music', 'Music'), ('ProductReview', 'ProductReview'), ('Q&A', 'Q&A'), ('Reaction', 'Reaction'), ('Sport', 'Sport'), ('Travel', 'Travel')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='field',
            field=models.CharField(choices=[('Comedy', 'Comedy'), ('Commentary', 'Commentary'), ('Educational', 'Educational'), ('Fashion', 'Fashion'), ('Food', 'Food'), ('Gaming', 'Gaming'), ('Interview', 'Interview'), ('Music', 'Music'), ('ProductReview', 'ProductReview'), ('Q&A', 'Q&A'), ('Reaction', 'Reaction'), ('Sport', 'Sport'), ('Travel', 'Travel')], max_length=50),
        ),
    ]

# Generated by Django 4.0.2 on 2022-06-05 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_comments_weekday_comment_posts_weekday_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='weekday_comment',
            field=models.IntegerField(blank=True, max_length=2, verbose_name='День недели коммента'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='weekday_post',
            field=models.IntegerField(blank=True, max_length=2, verbose_name='День недели поста'),
        ),
    ]

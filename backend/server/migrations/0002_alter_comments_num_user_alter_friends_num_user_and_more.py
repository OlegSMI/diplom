# Generated by Django 4.0.4 on 2022-06-01 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='num_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='server.infouser', verbose_name='Номер пользователя'),
        ),
        migrations.AlterField(
            model_name='friends',
            name='num_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='friends', to='server.infouser', verbose_name='Номер пользователя'),
        ),
        migrations.AlterField(
            model_name='geolocation',
            name='num_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='geolocation', to='server.infouser', verbose_name='Номер пользователя'),
        ),
        migrations.AlterField(
            model_name='infouser',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='num_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='server.infouser', verbose_name='Номер пользователя'),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='num_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='groups', to='server.infouser', verbose_name='Номер пользователя'),
        ),
    ]

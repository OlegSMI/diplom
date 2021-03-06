import datetime

from django.db import models


class InfoUser(models.Model):

    num_user = models.IntegerField(primary_key=True, 
                                    verbose_name='Номер пользователя'
                                    )
    user_id = models.CharField(max_length=100, 
                                verbose_name='Идентификатор'
                                )
    name = models.CharField(max_length=100, 
                            verbose_name='Имя'
                            )
    online_status = models.CharField(max_length=30, 
                                    verbose_name='Когда заходил'
                                    )
    status = models.CharField(max_length=100, 
                                verbose_name='Статус'
                                )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', 
                                verbose_name='Фото',
                                blank=True
                                )
    town = models.CharField(max_length=100, 
                            verbose_name='Город'
                            )
    languages = models.CharField(max_length=100, 
                                verbose_name='Язык'
                                )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Информацию о пользователе'
        verbose_name_plural='Информация о пользователе'


class UserGroup(models.Model):

    num_user = models.ForeignKey(InfoUser, 
                                on_delete=models.PROTECT, 
                                verbose_name='Номер пользователя', 
                                related_name='groups'
                                )
    groups = models.CharField(max_length=100, 
                                verbose_name='Группы', 
                                null=True, 
                                blank=True)

    def __str__(self):
        return self.groups

    class Meta:
        verbose_name='Группу'
        verbose_name_plural='Группы'


class Friends(models.Model):

    num_user = models.ForeignKey(InfoUser, 
                                on_delete=models.PROTECT, 
                                verbose_name='Номер пользователя', 
                                related_name='friends'
                                )
    friends = models.CharField(max_length=100, 
                                verbose_name='Друзья', 
                                null=True, 
                                blank=True
                                )

    def __str__(self):
        return self.friends
    
    class Meta:
        verbose_name='Друга'
        verbose_name_plural='Друзья'


class Posts(models.Model):

    num_user = models.ForeignKey(InfoUser, 
                                on_delete=models.PROTECT, 
                                verbose_name='Номер пользователя', 
                                related_name='posts'
                                )
    posts = models.CharField(max_length=100, 
                            verbose_name='Посты', 
                            null=True, 
                            blank=True
                            )
    timepost = models.TimeField(auto_now=False,
                                auto_now_add=False,
                                blank=True, 
                                verbose_name='Время поста',
                                default=datetime.time(16, 00)
                                )
    weekday_post = models.IntegerField(blank=True,
                                    verbose_name='День недели поста',
                                    )
                                    


    def __str__(self):
        return self.posts

    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'


class Comments(models.Model):

    num_user = models.ForeignKey(InfoUser, 
                                on_delete=models.PROTECT, 
                                verbose_name='Номер пользователя', 
                                related_name='comments'
                                )
    comments = models.CharField(max_length=100, 
                                verbose_name='Комментарии', 
                                null=True, 
                                blank=True
                                )
    timecomment = models.TimeField(auto_now=False,
                                auto_now_add=False,
                                blank=True,
                                verbose_name='Время коммента',
                                default=datetime.time(16, 00)
                                )
    weekday_comment = models.IntegerField(blank=True,
                                        verbose_name='День недели коммента',
                                        )

                                        
    def __str__(self):
        return self.comments

    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии'


class Geolocation(models.Model):

    num_user = models.ForeignKey(InfoUser,
                                on_delete=models.PROTECT, 
                                verbose_name='Номер пользователя', 
                                related_name='geolocation'
                                )
    location = models.CharField(max_length=100, 
                                verbose_name='Геолокации', 
                                null=True, 
                                blank=True
                                )

    def __str__(self):
        return self.location 
    
    class Meta:
        verbose_name='Геолокацию'
        verbose_name_plural='Геолокации'


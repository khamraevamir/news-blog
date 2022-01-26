from django.db import models
from django.db.models.fields import related
from django.utils import timezone
from django.shortcuts import render, redirect, reverse
from django.conf import settings
User = settings.AUTH_USER_MODEL



class Category(models.Model):
    title = models.CharField('Загаловок', max_length=250, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, related_name='category_posts', null=True, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField('Загаловок', max_length=250, null=True)
    body = models.TextField('Контент', null=True)
    image = models.FileField('Фото', null=True, blank=True)
    date = models.DateTimeField('Дата', default=timezone.now)
    
    
    class Meta:       
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title + ' Категория: '+ self.category.title




class Comment(models.Model):
    post = models.ForeignKey(Post,null=True, on_delete=models.CASCADE, related_name='post_comments', verbose_name='Post')
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='user_comments', verbose_name='User')
    body = models.TextField('Текст')  
    date = models.DateTimeField('Дата', default=timezone.now)
    

    class Meta:
        verbose_name = 'Коменнты'
        verbose_name_plural = 'Коменнты'

    def __str__(self):
        return self.user.username + self.post.title



class Favourite(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='favourite_users', verbose_name='Favourite')
    post =  models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='favourite_posts', verbose_name='Post')
    status = models.BooleanField('Status', default=False)

    
    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return self.user.username



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User',related_name='liked_users', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post',related_name='liked_posts', null=True)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Like'

    def __str__(self):
        return self.user.username



class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Users',related_name='disliked_users', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Posts',related_name='disliked_posts', null=True)

    class Meta:
        verbose_name = 'DisLike'
        verbose_name_plural = 'DisLike'

    def __str__(self):
        return self.user.username

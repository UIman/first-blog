'''
Модели отображают информацию о данных, с которыми вы работаете.
Содержат поля и поведение ваших данных.
Обычно одна модель представляет одну таблицу в базе данных.
'''
from django.db import models
from django.utils import timezone


class Post(models.Model):
    ''' Класс создания модели для БД '''
    class Meta():
        ''' Класс задает имя в таблице БД '''
        db_table = 'post'

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        ''' Метод публикации записи из чертежа '''
        self.published_date = timezone.now()
        # сохраняем в БД
        self.save()


    def approved_comments(self):
        ''' Метод возвращвет только одобренные комментарии '''
        return self.comments.filter(approved_comment=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    ''' Класс создания модели комментариев для БД '''
    class Meta():
        db_table = 'comments'

    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        ''' Функция одобрения комментария '''

        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

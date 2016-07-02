'''
Модели отображают информацию о данных, с которыми вы работаете.
Они содержат поля и поведение ваших данных.
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
        '''  '''
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        '''  '''
        return self.title

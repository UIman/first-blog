''' Файл настройки прав администратора '''
from django.contrib import admin
from .models import Post

# регистрируем модель для страницы администратора
admin.site.register(Post)

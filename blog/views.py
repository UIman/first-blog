''' Файл методов ответа на запрос пользователя '''
''' Соединяют шаблоны и модели: берут модели и передают их в шаблон '''
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):

    # сортировка по дате
    # render возарвщает список
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

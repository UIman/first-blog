''' Файл методов ответа на запрос пользователя '''
''' Соединяют шаблоны и модели: берут модели и передают их в шаблон '''
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    ''' Функция представления списка записей '''

    # сортировка по дате
    # render возарвщает список
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    ''' Функция детального представления записи '''

    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    ''' Класс создания формы для новой записи '''
    class Meta:
        ''' Класс указывает какая модель и поля должны быть в форме '''
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)

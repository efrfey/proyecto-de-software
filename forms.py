# blog/forms.py
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']  # Asegúrate de que estos campos sean los correctos

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Solo el campo de contenido para el comentario

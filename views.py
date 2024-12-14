from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import render
from .models import Post

def eventos(request):
    eventos_posts = Post.objects.filter(category='Eventos').order_by('-created_at')
    return render(request, 'blog/eventos.html', {'eventos_posts': eventos_posts})
def registro(request):
    return render(request, 'blog/registro.html')

def iniciar_sesion(request):
    return render(request, 'blog/iniciar_sesion.html')

def home(request):
    news_posts = Post.objects.filter(category='Noticias').order_by('-created_at')[:10]
    return render(request, 'blog/home.html', {'news_posts': news_posts, 'user': request.user})

def noticias(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.category = 'Noticias'
            post.save()
            return redirect('noticias')
    else:
        form = PostForm()

    posts = Post.objects.filter(category='Noticias').order_by('-created_at')
    return render(request, 'blog/noticias.html', {'posts': posts, 'form': form})

def eventos(request):
    posts = Post.objects.filter(category='Eventos').order_by('-created_at')
    return render(request, 'blog/eventos.html', {'posts': posts})

def contactos(request):
    return render(request, 'blog/contactos.html')

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'category']
    success_url = '/'

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_list')
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})


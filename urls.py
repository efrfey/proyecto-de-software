from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    # Otras rutas
    path('eventos/', views.eventos, name='eventos'),
]

urlpatterns = [
    path('', views.home, name='inicio'),  # Ruta para Inicio
    path('noticias/', views.noticias, name='noticias'),  # Ruta para Noticias
    path('eventos/', views.eventos, name='eventos'),  # Ruta para Eventos
    path('contactos/', views.contactos, name='contactos'),  # Ruta para Contáctanos
]
urlpatterns = [
    # Rutas para autenticación
    path('accounts/logout/', auth_views.LoginView.as_view(), name='logout'),
    
    # Otras rutas
    path('registro/', views.registro, name='registro'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('', views.home, name='inicio'),
    path('noticias/', views.noticias, name='noticias'),
    path('eventos/', views.eventos, name='eventos'),
    path('contactos/', views.contactos, name='contactos'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),

    
]
from django.urls import path
from . import views

app_name = 'core'   # <-- حتماً این خط را داشته باشید

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
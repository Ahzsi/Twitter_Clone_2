from django.urls import path, URLPattern
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:post_ID>/', views.delete, name='delete'),
    path('edit/<int:post_ID>/', views.edit, name='edit'),
    path('like/<int:post_ID>', views.LikePost, name='like')
]

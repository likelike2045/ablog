
from . import views
from django.urls import path
from theblog.views import (PostListView, PostDetailView, PostCreateView, 
	PostUpdateView, PostDeleteView, CategoryCreateView, Category2CreateView)

app_name = 'theblog'
urlpatterns = [

    path('',PostListView.as_view(), name='home'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('add-category/', CategoryCreateView.as_view(), name='add-category'),
    path('add-post/', PostCreateView.as_view(), name='add-post'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='update-post'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete-post'),
    path('create-category/', CategoryCreateView.as_view(), name='create-category'),
    
    path('create-category2/', Category2CreateView.as_view(), name='create-category2'),
    
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('like/<int:pk>', views.LikeView, name='like-post'),

    path('datetime/', views.current_datetime, name='date-time')
]


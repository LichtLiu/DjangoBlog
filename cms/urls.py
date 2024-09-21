from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('', views.home, name='home'),  # CMS Home
    # 显示文章列表
    #path('articles/', views.article_list, name='article_list'),

    # 显示单篇文章详情
    #path('article/<int:id>/', views.article_detail, name='article_detail'),

    # 创建新文章
    #path('article/new/', views.article_create, name='article_create'),

    # 编辑文章
    #path('article/<int:id>/edit/', views.article_edit, name='article_edit'),

    # 删除文章
    #path('article/<int:id>/delete/', views.article_delete, name='article_delete'),
]

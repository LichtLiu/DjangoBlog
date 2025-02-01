from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import CustomUserCreationForm, ArticleForm, SectionFormSet

from blog.models import Article

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # 使用 get 方法获取
        password = request.POST.get('password')  # 使用 get 方法获取

        if username and password:  # 确保用户名和密码都存在
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # 登录成功后重定向到主页
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})
        else:
            return render(request, 'login.html', {'error': 'Please enter both username and password'})
    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # 登出后重定向到登录页面

@login_required
def home(request):
    total_posts = Article.objects.count()

    # 計算一個月前的日期
    one_month_ago = timezone.now() - timedelta(days=30)
    
    # 獲取最近一個月內的文章
    recent_posts = Article.objects.filter(
        updatetime__gte=one_month_ago
    ).order_by('-updatetime')[:5]  # 取最新的5篇文章
    
    # 分頁處理
    all_posts = Article.objects.all().order_by('-updatetime')
    paginator = Paginator(all_posts, 3)  # 每頁顯示3篇文章
    
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # 如果頁碼不是整數，顯示第一頁
        posts = paginator.page(1)
    except EmptyPage:
        # 如果頁碼超出範圍，顯示最後一頁
        posts = paginator.page(paginator.num_pages)
    
    context = {
        'total_posts': total_posts,
        'recent_posts': recent_posts,
        'posts': posts
    }
    return render(request, 'home.html', context)


@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        formset = SectionFormSet(request.POST, instance=article)
        
        if form.is_valid() and formset.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()  # 保存多對多關係（標籤）
            formset.save()
            messages.success(request, '文章已成功更新！')
            return redirect('home')
    else:
        form = ArticleForm(instance=article)
        formset = SectionFormSet(instance=article)
    
    return render(request, 'article/article_edit.html', {
        'form': form,
        'formset': formset,
        'article': article
    })
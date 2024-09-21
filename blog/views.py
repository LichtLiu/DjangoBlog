from django.shortcuts import render, get_object_or_404
from .models import Homepage, Article

# Create your views here.
def index(request):
    index = get_object_or_404(Homepage, id=1) 
    latest_article = Article.objects.filter(is_top=True).order_by('-updatetime').first()
    articles = Article.objects.filter(is_top=True).order_by('-updatetime')[1:4]
    all_stories = Article.objects.filter(is_top=False).order_by('-updatetime')[:3]
    popular_articles = Article.objects.all().order_by('-views')[:4]
    return render(request,'index.html' ,{'index':index, 
                                         'latest_article': latest_article,
                                         'articles':articles,
                                         'all_stories':all_stories,
                                         'popular_articles':popular_articles,
                                         })


def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # 查找上一个文章
    previous_article = Article.objects.filter(id__lt=article.id).order_by('-id').first()
    previous_three_articles = Article.objects.filter(id__lt=article.id).order_by('-id')[1:4]
    return render(request, 'article.html', {'article': article,
                                            'previous_article':previous_article,
                                            'previous_three_articles':previous_three_articles
                                            })

def about(request):
    index = get_object_or_404(Homepage, id=1) 
    article = get_object_or_404(Article, id=4)
    previous_article = Article.objects.all().order_by('-id').first()
    previous_three_articles = Article.objects.all().order_by('-id')[1:4]
    return render(request, 'about.html',{
                                        'index':index,
                                        'article':article, 
                                        'previous_article':previous_article,
                                        'previous_three_articles':previous_three_articles
                                        })
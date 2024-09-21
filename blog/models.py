from django.db import models
from django.contrib.auth.models import User  

# Index
class Homepage(models.Model):
    title = models.CharField(max_length=200)  
    content = models.TextField()
    image =  models.ImageField(upload_to='page_images/', null=True, blank=True) 

    def __str__(self):
        return self.title  

# 類別
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Tag
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Article
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # 
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    is_top = models.BooleanField(default=False) #是否置頂
    views = models.IntegerField(default=0)  # 瀏覽次數
    updatetime = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE, default=1)
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)

    

    def __str__(self):
        return self.title

class Section(models.Model):
    ARTICLE_SECTION_TYPE_CHOICES = [
        ('H1', 'Header1'),
        ('H2', 'Header2'),
        ('H3', 'Header3'),
        ('P', 'paragraph')
    ]

    article = models.ForeignKey(Article, related_name='sections', on_delete=models.CASCADE)
    section_type = models.CharField(max_length=2, choices=ARTICLE_SECTION_TYPE_CHOICES)
    content = models.TextField(blank=True)  # 用於內文的內容
    order = models.IntegerField(default=0)  # 用于排序的字段

    def __str__(self):
        if self.section_type in ['H1', 'H2', 'H3']:
            return f"{self.get_section_type_display()}: {self.content}"
        return f"{self.get_section_type_display()}: {self.content[:30]}..."  # 顯示內文的前30個字符
    class Meta:
        ordering = ['order']  # default order 



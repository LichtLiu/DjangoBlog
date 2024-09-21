from django.contrib import admin

from .models import Homepage

from .models import Article, Section, Category, Tag, Article
# Register your models here.

#Index
admin.site.register(Homepage)



admin.site.register(Tag)

#Article
class SectionInline(admin.TabularInline):
    model = Section
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'updatetime', 'is_top', 'views')  # Article show id
    list_filter = ('category', 'tags', 'is_top', 'updatetime')
    search_fields = ('title', 'content')
    ordering = ('-updatetime',)
    inlines = [SectionInline]
    filter_horizontal = ('tags',)
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'category', 'tags', 'content', 'image')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('is_top', 'views'),
        }),
    )


#Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
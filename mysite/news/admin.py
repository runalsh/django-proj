from django.contrib import admin

# Register your models here.
from .models import News, Category



class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title' )
    search_fields = ('content', 'title')
    list_editable  =  ('is_published',)
    list_filter = ('category', 'is_published')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title' )
    search_fields = ('content',)    

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)









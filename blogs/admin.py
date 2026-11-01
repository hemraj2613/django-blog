from django.contrib import admin
from .models import Category, Blog

# automatic slug generation 
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'updated_at')

admin.site.register(Category, CategoryAdmin)

admin.site.register(Blog, BlogAdmin)
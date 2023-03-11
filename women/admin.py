from django.contrib import admin

from .models import *

class WomenAdmin(admin.ModelAdmin): # вспомогательный класс, чтобы в админке список статей был с этими полями
    list_display = ('id', 'title', 'cat', 'photo', 'time_create', 'is_published')
    list_display_links = ('id', 'title') # какие поля будут ссылками
    search_fields = ('title', 'content') # по каким полям делать поиск
    list_editable = ('is_published',) # какие поля можно редактировать прямо в списке
    list_filter = ('is_published', 'time_create') # фильтр справа: по этим полям можно фильтровать статьи в списке
    prepopulated_fields = {"slug": ("title",)}  # автоматическая генерация slug в админке

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',) # нужна запятая, т.к. всего один элемент, а это должен быть кортеж
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)

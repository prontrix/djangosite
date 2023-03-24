from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class WomenAdmin(admin.ModelAdmin): # вспомогательный класс, чтобы в админке список статей был с этими полями
    list_display = ('id', 'title', 'cat', 'get_html_photo', 'time_create', 'is_published')
    list_display_links = ('id', 'title') # какие поля будут ссылками
    search_fields = ('title', 'content') # по каким полям делать поиск
    list_editable = ('is_published',) # какие поля можно редактировать прямо в списке
    list_filter = ('is_published', 'time_create') # фильтр справа: по этим полям можно фильтровать статьи в списке
    prepopulated_fields = {"slug": ("title",)}  # автоматическая генерация slug в админке
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update') # порядок и список полей при редактировании статьи
    readonly_fields = ('time_create', 'time_update', 'get_html_photo') # нередактируемые поля. Нужно прописывать, если хотим добавить в fields
    save_on_top = True # панель сохранения статьи будет дублироваться сверху

    def get_html_photo(self, object): # делаем метод для вывода картинок статей, а не просто ссылок
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>") # mark_safe - не экранировать теги

    get_html_photo.short_description = "Миниатюра"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',) # нужна запятая, т.к. всего один элемент, а это должен быть кортеж
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админ-панель сайта о женщинах'
admin.site.site_header = 'Админ-панель сайта о женщинах 2'

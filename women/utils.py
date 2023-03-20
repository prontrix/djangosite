from django.db.models import Count

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

# класс, чтобы убрать повторяющийся код
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('women')) # дополнительно прочитываем количество статей в категории (Count)
        user_menu = menu.copy()
        if not self.request.user.is_authenticated: # проверяем авторизован ли пользователь, и если нет, то убираем пункт "Добавить статью"
            user_menu.pop(1)
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
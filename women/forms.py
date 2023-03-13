from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddPostForm(forms.ModelForm):
    # добавляем конструктор, если хотим переопределить поля, например, выпадающий список
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Women # взаимодействие с оновной моделью
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat'] # какие поля будут в форме, можно __all__, чтобы были все
        # стили оформления отдельных полей
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    # clean_* - пользовательский валидатор для конкретного поля формы
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title
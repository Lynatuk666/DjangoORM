from multiprocessing.resource_tracker import register

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag







class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        if len(self.forms) == 0:
            raise ValidationError('Не определены теги')
        main_count = 0
        for form in self.forms:
            if form.cleaned_data == {}:
                continue  # пропускаем пустые формы
            if form.cleaned_data['is_main']:
                main_count += 1

        if main_count > 1:  # основная форма может быть только одна
            raise ValidationError('Есть несколько основных тегов')

        elif main_count == 0: # основная форма обязательна
            raise ValidationError('Нет основных тегов')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
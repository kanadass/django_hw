from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_list = []
        for form in self.forms:
            if len(form.cleaned_data) > 0:
                is_main_list.append(form.cleaned_data['is_main'])
        if is_main_list.count(True) > 1:
            raise ValidationError('Основным может быть только один раздел.')
        if is_main_list.count(True) == 0:
            raise ValidationError('Укажите основной раздел.')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


admin.site.register(Tag)
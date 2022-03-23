from django import forms

import core.models


class BookSearch(forms.Form):
    name = forms.CharField(label='Название', required=False)
    min_pages = forms.IntegerField(label='Кол-во страниц', required=False, help_text='Минимальное кол-во страниц')

    def clean(self):
        return forms.ValidationError('Ошибка!')

class BookEdit(forms.ModelForm):
    class Meta:
        model = core.models.Book
        fields = '__all__'



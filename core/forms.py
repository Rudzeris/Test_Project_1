from django import forms


class BookSearch(forms.Form):
    name = forms.CharField(label='Название', required=False, widget=forms.Textarea)
    min_pages = forms.IntegerField(label='Кол-во страниц', required=False, help_text='Минимальное кол-во страниц')

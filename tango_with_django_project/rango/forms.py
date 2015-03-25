from django import forms
from django.models import Page, Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='Please enter the category name.')
    views = form.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = form.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = form.CharField(widget=forms.HiddenInput(), required=False)


    class Meta:
        model = Category
        fields = ('name',)


class PageForm(form.ModelForm):
    title = forms.CharField(max_length=128, help_text='Please enter the title of the page.')
    url = form.URLField(max_length=200, help_text='Please enter the URL of the page.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)


    class Meta:
        model = Page
        exclude = ('category',)


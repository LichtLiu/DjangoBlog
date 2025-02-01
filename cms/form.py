from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from blog.models import Article, Section
from django.forms import inlineformset_factory

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'tags', 'image', 'is_top']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'is_top': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

SectionFormSet = inlineformset_factory(
    Article, Section,
    fields=['section_type', 'content', 'order'],
    extra=1,
    can_delete=True,
    widgets={
        'section_type': forms.Select(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'class': 'form-control'}),
        'order': forms.NumberInput(attrs={'class': 'form-control'})
    }
)
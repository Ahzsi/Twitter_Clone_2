from django import forms
from .models import Post

class ContentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
from django import forms
from .models import Post

""" ^import forms and our Post model.
    Create a from called PostForm of type ModelForm
    tell it (class Meta) to use our Post model to create the form,
    spec fields in the form.
"""
"""class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'summary', 'content', 'tips'}
"""

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {
            'title': "forms.CharField(widget=forms.TextInput(attrs={'class': 'is-success'})",
            'summary': "forms.CharField(widget=forms.TextInput(attrs={'class': 'textarea is-half is-success'})",
            'content': "forms.CharField(widget=forms.TextInput(attrs={'class': 'textarea'})",
            'tips': "forms.CharField(widget=forms.TextInput(attrs={'class': 'textarea'})",
        }

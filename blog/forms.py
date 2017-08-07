from django import forms
from .models import Post

""" ^import forms and our Post model.
    Create a from called PostForm of type ModelForm
    tell it (class Meta) to use our Post model to create the form,
    spec fields in the form.
"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'summary', 'content'}

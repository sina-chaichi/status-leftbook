from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
            'class': 'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = models.Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
            'class': 'editable medium-editor-textarea commentcontent'})
        }

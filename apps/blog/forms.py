from django import forms
from .models import Comment
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    content = forms.CharField(required=True)

    class Meta:
        fields = ['content']
        model = Comment

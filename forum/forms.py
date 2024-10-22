# forms.py

from django import forms
from .models import Topic, Comment, Profile

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ProfileForm(forms.ModelForm):   
    class Meta:
        model = Profile
        fields = ['bio'] 

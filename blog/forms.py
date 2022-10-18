from .models import Comment
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment
from django import forms


class PostForm(ModelForm):
    """
    The PostForm class defines the user form output for the Post model class.
    """
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        """
        The Meta class defines which model is associated and from that model,
        which fields will be accessible to the user.
        """
        model = Post
        fields = (
            'title',
            'featured_image',
            'excerpt',
            'meal_type',
            'food_type',
            'content'
        )
 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
from django.db import models
from tinymce.models import HTMLField
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = RichTextUploadingField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

#
# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ['content']
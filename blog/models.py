from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.
User = get_user_model()

class Post(models.Model):
  title = models.CharField(max_length=200)
  content = RichTextUploadingField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  featured_image = models.ImageField(upload_to="Featured_Images", default='')
  created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)


  def __str__(self):
    return self.title 



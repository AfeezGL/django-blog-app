from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
from autoslug import AutoSlugField

class Article(models.Model):
    image = models.ImageField(blank = True, null = True)
    title = models.CharField(max_length = 350)
    body = models.TextField(null = True, blank = True)
    slug = AutoSlugField(populate_from='title')
    pub_date = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title

    @property
    def short(self):
        return self.body[3:120]
    

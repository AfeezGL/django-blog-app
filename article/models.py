from django.db import models
from autoslug import AutoSlugField

class Article(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length = 400)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now = True)
    update_date = models.DateTimeField(auto_now_add = True)
    slug = AutoSlugField(populate_from = "title")
    @property
    def short_text(self):
        return self.body[0:150]
        
    def __str__(self):
        return self.title

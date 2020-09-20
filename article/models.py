from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
from hitcount.models import HitCount
from hitcount.models import HitCountMixin
from django.contrib.contenttypes.fields import GenericRelation
from autoslug import AutoSlugField

class Article(models.Model, HitCountMixin):
    image = models.ImageField(blank = True, null = True)
    title = models.CharField(max_length = 350)
    body = RichTextUploadingField(null = True, blank = True)
    slug = AutoSlugField(populate_from='title')
    pub_date = models.DateTimeField(auto_now = True)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
        )
    def __str__(self):
        return self.title

    @property
    def short(self):
        return self.body[3:120]
    
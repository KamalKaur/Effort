from django.db import models
from django.db.models import permalink
from django.forms import ModelForm

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField() #db_index=True, auto_now_add=True
#    category = models.ForeignKey(Category)  --- showed error , had to drop and recreate tables

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class BlogForm(ModelForm):
	class Meta :
		model=Blog
		

class Category(models.Model):
    blog=models.ForeignKey(Blog)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class CategoryForm(ModelForm):
	class Meta :
		model=Category
		

from django.utils.html import escape, format_html, format_html_join
from django.db import models

# Create your models here.
class ImageStore(models.Model):
    ImageOrder = models.IntegerField(default=9999)
    ImageURL = models.CharField(max_length=300)
    ImageREF = models.CharField(max_length=300)
    ImageTitle = models.CharField(max_length=200)
    ImageKeyword = models.CharField(max_length=100,default='google image')
    ImageURL.allow_tags = True

    def image_tag(self):
        #return '<img src="%s" />' % self.ImageURL
        return format_html(
            '<img src="{url}" style="width:250px">',
            url=self.ImageURL)

        image_tag.short_description = 'Image'
        image_tag.allow_tags = True
    def __str__(self):              # __unicode__ on Python 2
        return self.ImageTitle

class ImageStage(models.Model):
    ImageOrder = models.IntegerField(default=9999)
    ImageURL = models.CharField(max_length=300)
    ImageREF = models.CharField(max_length=300)
    ImageTitle = models.CharField(max_length=200)
    ImageKeyword = models.CharField(max_length=100,default='google image')
    ImageURL.allow_tags = True

    def image_tag(self):
        #return '<img src="%s" />' % self.ImageURL
        return format_html(
            '<img src="{url}" style="width:250px">',
            url=self.ImageURL)

        image_tag.short_description = 'Image'
        image_tag.allow_tags = True
    def __str__(self):              # __unicode__ on Python 2
        return self.ImageTitle

class ImageSelected(models.Model):
    ImageOrder = models.IntegerField(default=9999)
    ImageURL = models.CharField(max_length=300)
    ImageREF = models.CharField(max_length=300)
    ImageTitle = models.CharField(max_length=200)
    ImageKeyword = models.CharField(max_length=100,default='google image')
    ImageURL.allow_tags = True

    def image_tag(self):
        #return '<img src="%s" />' % self.ImageURL
        return format_html(
            '<img src="{url}" style="width:250px">',
            url=self.ImageURL)

        image_tag.short_description = 'Image'
        image_tag.allow_tags = True
    def __str__(self):              # __unicode__ on Python 2
        return self.ImageTitle

class Amazon(models.Model):
    asin = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)

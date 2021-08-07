from django import forms
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor.fields import RichTextFormField
# Create your models here.

class BasicForm(models.Model):
    title = models.CharField(max_length=25,default=None,blank=True)
    username = models.CharField(max_length=25,default=None,blank=True)
    realtext = RichTextField()

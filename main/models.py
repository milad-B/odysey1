from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from ckeditor_uploader.fields import RichTextUploadingField
# models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

from django.utils.translation import gettext_lazy as _
import jdatetime
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Homepage(models.Model):
    homepagename = models.CharField(max_length=200 ,default=0)
    selected = models.IntegerField(default=0)
    def __str__(self):
        return str(self.selected)
    img_url = models.ImageField()


class Sticky(models.Model):
    homepage = models.ForeignKey(Homepage,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.title)
    icon_url = models.CharField(max_length=200 ,default=0)
    title = models.CharField(max_length=200 ,default=0)
    text = models.TextField(max_length=200 ,default=0)
    url = models.CharField(max_length=200 ,default=0)

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField()

    def __str__(self):
        return self.name
    name = models.CharField(max_length=200 ,default=0)
    number = models.IntegerField(default=0)
    address = models.TextField(max_length=200 ,default=0)


class Reserve(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.confirm) +'|'+ str(self.user.username) +'|'+ str(self.service) +'|'+ str(self.date) +'|'+ str(self.hour)
    #advice therapy
    service = models.CharField(max_length=200 ,default="advice")
    detail = models.TextField(max_length=200 ,default=0)
    date = models.DateField()
    hour = models.TimeField()

    def shamsidate(self):
        jalili_date =  jdatetime.date.fromgregorian(day=self.date.day,month=self.date.month,year=self.date.year)
        return jalili_date
        
        
    #confirmed denied pending
    confirm = models.CharField(max_length=200 ,default="confirmed")



class Bpost(models.Model):
    postid = models.IntegerField(default=1)
    title = models.CharField( max_length=250,
        null=False, blank=False
    )
    subject = models.CharField(max_length=200 ,default='psy')
    body = RichTextUploadingField()
    def __str__(self):
        return 'id:'+str(self.pk)+'    title:'+str(self.title )

class Comment(models.Model):
    post = models.ForeignKey(Bpost,on_delete=models.CASCADE)
    def __str__(self):
        return  str(self.name)
    
    img = models.ImageField(default='/static/guestprofile.jpg')
    name = models.CharField(max_length=200 ,default=0)
    email = models.CharField(max_length=200 ,default=0)
    Comment = models.TextField(max_length=200 ,default=0)
    date = models.DateField(default=timezone.now())
    def shamsidate(self):
        jalili_date =  jdatetime.date.fromgregorian(day=self.date.day,month=self.date.month,year=self.date.year)
        return jalili_date

class Keywords(models.Model):
    post = models.ForeignKey(Bpost,on_delete=models.CASCADE)
    word = models.CharField(max_length=200 ,default=0)
    def __str__(self):
        return str(self.post.title) +'|'+ str(self.word)



from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Pray_tb(models.Model):
    # books = [
    #     ('john','john'),
    #     ('jacob','jacob'),
    #     ('james','james'),
    # ]
    Date_Created = models.DateTimeField(timezone.now)
    Adhola_Prayer = models.TextField()
    # Book = models.CharField(max_length=45,choices=books,default='jacob')
    Book = models.CharField(max_length=45)
    img = models.ImageField(upload_to='pic')
    Posted_by = models.CharField(max_length=45)
    English_Prayer = models.TextField()
    daily_prayer_detail = models.TextField()
    slug = models.SlugField(max_length=250 ,unique = True)

    def __str__(self):
        return self.Adhola_Prayer
      



class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    comment = models.TextField()
    comment_date = models.DateTimeField(timezone.now)






from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    # text = models.TextField()
    image = models.ImageField(upload_to='gallery/')
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Shop(models.Model):
    shop_title = models.CharField(max_length=200)
    shop_image = models.ImageField(upload_to='gallery/')
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.shop_title

class Paint(models.Model):
    paint_title = models.CharField(max_length=200)
    paint_title_rus = models.CharField(max_length=200)
    paint_text = models.CharField(max_length=200)
    paint_image = models.ImageField(upload_to='gallery/')
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.paint_title
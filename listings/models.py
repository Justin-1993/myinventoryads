from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

# Create your models here.
from categories.models import Categorie


class Listing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    category = models.ForeignKey(Categorie, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    part_number = models.CharField(max_length=40)
    contact_email = models.EmailField(max_length=100)
    website_url = models.URLField(max_length=200)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=6)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    
    def __str__(self):
        return self.title
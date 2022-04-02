from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Youtuber(models.Model):
    crew_choises = (
        ('solo', 'solo'),
        ('small', 'small'),
        ('large', 'large'),
        ('medium', 'medium'),
    )

    camera_choises = (
        ('nikon', 'nikon'),
        ('cannon', 'cannon'),
        ('sony', 'sony'),
        ('fuji', 'fuji'),
        ('others', 'others'),
    )

    catagory_choises = (
        ('programming', 'programming'),
        ('cooking', 'cooking'),
        ('flaming', 'flaming'),
        ('cinema', 'cinema'),
        ('teaching', 'teaching'),
        ('comedy', 'comedy'),
    )

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/youtubers/%Y/%m/%d/')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    crew = models.CharField(choices=crew_choises, max_length=255)
    camera = models.CharField(choices=camera_choises, max_length=255)
    age = models.IntegerField()
    hight = models.IntegerField()
    subs_count = models.IntegerField()
    catagory = models.CharField(choices=catagory_choises, max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

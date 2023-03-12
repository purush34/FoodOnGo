from django.db import models

# Create your models here.


class HotelMenu(models.Model):

    restaurents = [
        ('Andhra Ruchulu', 'Andhra Ruchulu'),
        ('Love sugar', 'Love sugar'),
        ('Amritam', 'Amritam'),
        ('Cheta shop', 'Cheta shop'),
    ]
    category = [
        ('Vegetarian', 'Vegetarian'),
        ('Non-Vegetarian', 'Non-Vegetarian'),
    ]

    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100, choices=category, default='Vegetarian')
    description = models.TextField()
    image = models.ImageField(upload_to='static/images/')
    available = models.BooleanField(default=True)
    # HotelName = models.options.DEFAULT_NAMES = ('HotelName',"Andhra Ruchulu","Love sugar","Amritam","Cheta shop","Casa blanka","Spicy villa",)
    HotelName = models.CharField(max_length=100, choices=restaurents, default='Andhra Ruchulu')

    def __str__(self):
        return self.name
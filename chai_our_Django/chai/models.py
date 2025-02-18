from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML' , 'MASALA'),
        ('KL' , 'KADAK'),
        ('IL' , 'IRANI'),
        ('PL' , 'PLAIN'),
        ('SL' , 'SUGARLESS'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(default = '')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='chai/images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES )
    def __str__(self):
        return self.name
    
    
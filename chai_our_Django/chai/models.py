from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    


# one to many relationship

class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE , related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField()
    review = models.TextField(default = '')
    comment = models.TextField(default = '')
    def __str__(self):
        return f'{self.chai.name} review by {self.user.username}'
    
    
    


# many to many relationship

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety , related_name='stores')
    
    def __str__(self):
        return self.name
    
    
# one to one relationship

class ChaiCertification(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE)
    certification_number = models.CharField(max_length=100)
    date_issued = models.DateTimeField(default=timezone.now)
    valid_till = models.DateTimeField()
    def __str__(self):
        return f'CERTIFICATION FOR {self.name.chai}'
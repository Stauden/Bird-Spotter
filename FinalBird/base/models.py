from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
        #Note: change to nulls false when migrating
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    data = models.TextField(null=True, blank=True)

    wingspan = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    species = models.CharField(max_length=25,  blank=True, null=True)
    sex = models.CharField(max_length=1,  blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    injured = models.BooleanField(default=False, null=True)
    

    def __str__(self):
        #self is string r(null=False, blank=Trueepresetation of model
        return self.title
    
    class Meta:
        #orders model by the complete status from the above class
        #sends to bottom
        #orders query set
        ordering = ['complete']



from django.contrib.auth.models import User
from django.db import models


class Categories(models.Model):
    categories = models.CharField(max_length=30)                                        


class Ads(models.Model):
    date_time_generation = models.DateTimeField(auto_now_add=True)                      
    header = models.CharField(max_length=250)                                          
    text_and_multimedia = models.TextField()                           
    id_users = models.ForeignKey(User, on_delete=models.CASCADE)                      
    id_categories = models.ForeignKey(Categories, on_delete=models.CASCADE)             

class Reviews(models.Model):
    text = models.TextField()                                                           
    id_users_rev = models.ForeignKey(User, on_delete=models.CASCADE)                    
    id_ads = models.ForeignKey(Ads, on_delete=models.CASCADE)                           
    rev_status = models.BooleanField(default=False)                                     

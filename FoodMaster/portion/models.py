from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

from FoodMaster.food.models import Food

# Create your models here.
class Portion(models.Model):

    user = models.ForeignKey(User)
    food = models.ForeignKey(Food)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

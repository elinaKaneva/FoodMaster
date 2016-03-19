from django.db import models

# Create your models here.
class Food(models.Model):

    name = models.CharField(max_length=128)
    kcal = models.FloatField()
    carb = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return "{name},{kcal},{carb},{protein},{fat}".format(name=self.name,
                                                             kcal=self.kcal,
                                                             carb=self.carb,
                                                             protein=self.protein,
                                                             fat=self.fat)


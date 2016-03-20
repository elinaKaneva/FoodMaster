from django.contrib import admin

from FoodMaster.food.models import Food

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'kcal', 'carb', 'protein', 'fat')
    search_fields = ['name']

admin.site.register(Food, FoodAdmin)
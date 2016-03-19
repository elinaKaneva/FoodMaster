from django.http import JsonResponse
from django.shortcuts import render, redirect

from FoodMaster.portion.models import Portion
from FoodMaster.food.models import Food


# Create your views here.
def list_portions(request):
    portions = Portion.objects.filter(user=request.user).select_related()
    return render(request, "portion/list_portions.html", {"portions": portions})

def new_portion(request):
    # Adding new portion to the list with portions
    if request.method == "POST":
        food = Food.objects.get(name=request.POST["name"])
        Portion.objects.create(user=request.user, food=food, amount=request.POST["amount"])

        return render(request, "portion/new_portion.html", {"message": "New portion has been added!"})

    return render(request, "portion/new_portion.html", {})
from django.http import JsonResponse
from django.shortcuts import render, redirect

from FoodMaster.food.models import Food


# Create your views here.
def list_foods(request):
    foods = Food.objects.all()
    return render(request, "food/list_foods.html", {"foods": foods})

def new_food(request):
    # Adding new food to the list with foods
    if request.method == "POST":
        food_record = { k: v for k, v in request.POST.items() if k != "csrfmiddlewaretoken"}
        print("THIS ONE!!!",request.POST["name"])

        Food.objects.create(**food_record)

        return render(request, "food/new_food.html", {"message": "New food has been added!"})

    return render(request, "food/new_food.html", {})


def food_input(request):
    # Autocomplete function
    if request.method == "GET":
        mathing_food_objects = Food.objects.filter(name__contains=request.GET.get("lookFor",None))
        matching_food_names = [x.name for x in mathing_food_objects]
        matching_food_nutritions = [[x.kcal, x.carb, x.protein, x.fat] for x in mathing_food_objects]

    return JsonResponse({'foods': matching_food_names,
                         'nutritions': matching_food_nutritions})
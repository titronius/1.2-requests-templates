from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

import calculator.recipes_list as recipes_list

def get_dishes(request):
    CONTENT = list(map(lambda x: x , recipes_list.DATA.keys()))
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'dishes': page
    }
    return render(request, 'dishes/index.html', context)

def get_recipe(request, dish_name):
    if dish_name in recipes_list.DATA:
        servings = int(request.GET.get("servings", 1))
        ingridients = {k: round(v * servings,1) for k, v in recipes_list.DATA[dish_name].items()}
        context = {
          'recipe': ingridients,
          'dish_name': dish_name
        }
        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponse('Рецепт не найден')


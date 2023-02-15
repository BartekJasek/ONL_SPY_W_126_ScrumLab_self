import random
from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Recipe, Plan, RecipePlan


class IndexView(View):
    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "index.html", ctx)


def homepage(request):
    recipes = list(Recipe.objects.all())
    for i in range(3):
        random.shuffle(recipes)
    if request.method == 'GET':
        template = loader.get_template('index.html')
        context = {'recipes': recipes[0:1]}
        return HttpResponse(template.render(context, request))


def dashboard(request):
    recipenumbers = Recipe.objects.count()
    plannumbers = Plan.objects.count()

    template = loader.get_template('dashboard.html')
    context = {
        "plannumbers": plannumbers,
        "recipenumbers": recipenumbers,
    }
    return HttpResponse(template.render(context, request))


def recipedetails(request, id):
    rdetails = Recipe.objects.get(id=id)
    template = loader.get_template('app-recipe-details.html')

    context = {'rdetails': rdetails}
    return HttpResponse(template.render(context, request))


def recipelist(request):
    # recipe = Recipe.objects.all().order_by('-votes')
    recipes = Recipe.objects.all().order_by('-votes', '-created')
    p = Paginator(recipes, 50)
    page = request.GET.get('page')
    recipes_list = p.get_page(page)
    nums = "a" * recipes_list.paginator.num_pages
    if request.method == 'GET':
        template = loader.get_template('app-recipes.html')
        context = {"recipes": recipes, 'recipes_list': recipes_list, 'nums': nums}
        return HttpResponse(template.render(context, request))


def recipemodify(request, id):
    template = loader.get_template('app-edit-recipe.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
    

def planlist(request):
    template = loader.get_template('app-schedules.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def plandetails(request, id):
    plan_id = int(id)
    plan = Plan.objects.get(id=plan_id)
    recipesplan = RecipePlan.objects.filter(plan_id=plan_id).order_by('day_name_id', 'order')
    days_list = []
    day_order_dict = {}

    for rp in recipesplan:
        if rp.day_name not in day_order_dict.keys():
            days_list.append(rp.day_name)
            day_order_dict[rp.day_name] = [rp.order]
        else:
            if rp.order not in day_order_dict[rp.day_name]:
                day_order_list = day_order_dict[rp.day_name]
                day_order_list.append(rp.order)
                day_order_dict[rp.day_name] = day_order_list

    if request.method == 'GET':
        template = loader.get_template('app-details-schedules.html')
        context = {
            'plan': plan,
            'recipesplan': recipesplan,
            'days_list': days_list,
            'day_order_dict': day_order_dict
        }
        return HttpResponse(template.render(context, request))


def recipeadd(request):
    txt = ''
    template = loader.get_template('app-add-recipe.html')
    context = {
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        ingredients = request.POST.get('ingredients')
        description = request.POST.get('description')
        preparation_time = request.POST.get('preparation_time')
        if name and ingredients and description and preparation_time:
            if preparation_time.isdigit:
                Recipe.objects.create(name=name,
                                      ingredients=ingredients,
                                      description=description,
                                      preparation_time=preparation_time)
                return redirect(f"/recipe/list/")
        txt = 'Wypełnij poprawnie wszystkie pola'
        context = {
            'txt': txt
            }
        return HttpResponse(template.render(context, request))

    return HttpResponse(template.render(context, request))


def planadd(request):
    template = loader.get_template('app-add-schedules.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def planaddrecipe(request):
    template = loader.get_template('app-schedules-meal-recipe.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


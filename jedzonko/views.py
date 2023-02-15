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
    plan = Plan.objects.latest('created')

    template = loader.get_template('dashboard.html')
    context = {
        "plannumbers": plannumbers,
        "recipenumbers": recipenumbers,
        "plan": plan,
    }
    return HttpResponse(template.render(context, request))


def recipedetails(request, id):
    rdetails = Recipe.objects.get(id=id)
    template = loader.get_template('app-recipe-details.html')

    context = {'rdetails': rdetails}
    return HttpResponse(template.render(context, request))


def recipelist(request):
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
    plans = Plan.objects.all().order_by('name')
    p = Paginator(plans, 50)
    page = request.GET.get('page')
    plans_list = p.get_page(page)
    nums = "a" * plans_list.paginator.num_pages
    if request.method == 'GET':
        template = loader.get_template('app-schedules.html')
        context = {'plans': plans, 'plans_list': plans_list, 'nums': nums}
        return HttpResponse(template.render(context, request))


def plandetails(request, id):
    template = loader.get_template('app-details-schedules.html')
    context = {
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
    txt = ''
    template = loader.get_template('app-add-schedules.html')
    context = {
    }
    if request.method == 'GET':
        return render(
            request,
            'app-add-schedules.html',
            context={}
        )
    if request.method == 'POST':
       name = request.POST.get('name')
       description = request.POST.get('description')
       if name and description:
            Recipe.objects.create(name=name,
                                  description=description)
            return redirect(f"/plan/add/")
       txt = 'Wypełnij wszystkie pola'
       context = {
           'txt': txt
           }
       return HttpResponse(template.render(context, request))

    return HttpResponse(template.render(context, request))



def planaddrecipe(request):
    template = loader.get_template('app-schedules-meal-recipe.html')
    if request.method == 'POST':

        RecipePlan.objects.create(meal_name=request.POST.get('name'),
                                  recipe=request.POST.get('recipe'),
                                  plan=request.POST.get('choosePlan'),
                                  order=request.POST.get('number'),
                                  day_name=request.POST.get('day')),
    elif request.method == 'GET':
        plans = Plan.objects.all()
        recipes = Recipe.objects.all()
        days = RecipePlan.objects.all()

    context = {
        "plans": plans,
        "recipes": recipes,
        "days": days
    }
    return HttpResponse(template.render(context, request))

import random
from datetime import datetime
from django.shortcuts import render
from django.views import View
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Recipe, Plan


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
    template = loader.get_template('app-details-schedules.html')


def recipeadd(request):
    template = loader.get_template('app-add-recipe.html')
    if request.method == 'POST':
        Recipe.objects.create(name=request.POST.get('name'),
                              ingredients=request.POST.get('ingredients'),
                              description=request.POST.get('description'),
                              preparation_time=request.POST.get('preparation_time'))
    context = {
    }
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


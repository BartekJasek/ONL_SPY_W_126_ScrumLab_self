import random
from datetime import datetime
from django.shortcuts import render
from django.views import View
from django.template import loader
from django.http import HttpResponse
from jedzonko.models import Recipe, Plan


class IndexView(View):
    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


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


def receipelist(request):
    template = loader.get_template('test.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def planlist(request):
    template = loader.get_template('test.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def receipeadd(request):
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
    template = loader.get_template('test.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def planaddreceipe(request):
    template = loader.get_template('test.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

# def carousel(request):
#     recipes = Recipe.objects.all()
#     recipes = list(Recipe.objects.all())
#     recipe = random.sample(recipes, 1)
#     return render(request, 'index.html', {'recipes': recipes})

import random
from datetime import datetime

from django.shortcuts import render
from django.views import View
from django.template import loader
from django.http import HttpResponse
from .models import Recipe



class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


def homepage(request):
    recipes = Recipe.objects.all()
    recipes = list(Recipe.objects.all())
    random.shuffle(recipes)
    if request.method == 'GET':
        template = loader.get_template('index.html')
        context = {'recipes': recipes}
        return HttpResponse(template.render(context, request))


def dashboard(request):
    template = loader.get_template('dashboard.html')
    context = {
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
    template = loader.get_template('test.html')
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





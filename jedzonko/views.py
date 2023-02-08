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
    template = loader.get_template('index.html')
    context = {
        #'recipe': Recipe.objects.all()
    }
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
def carousel(request):
    recipe = list(Recipe.objects.all())
    recipe = random.sample(recipe, 1)
    return render(request, 'index.html', {'recipe': recipe})





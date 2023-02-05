from datetime import datetime

from django.shortcuts import render
from django.views import View
from django.template import loader
from django.http import HttpResponse


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


def homepage(request):
    template = loader.get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

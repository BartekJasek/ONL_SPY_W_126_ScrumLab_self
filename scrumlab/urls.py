"""scrumlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from jedzonko.views import IndexView
from jedzonko import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', IndexView.as_view()),
    path('', views.homepage),
    path('main/', views.dashboard),
    path('recipe/<int:id>/', views.recipedetails),
    path('recipe/list/', views.recipelist, name='recipes'),
    path('recipe/add/', views.recipeadd),
    path('recipe/modify/<int:id>/', views.recipemodify),
    path('plan/list/', views.planlist),
    path('plan/<int:id>/', views.plandetails),
    path('plan/add/', views.planadd),
    path('plan/add-recipe/', views.planaddrecipe)
]

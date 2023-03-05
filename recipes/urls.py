from django.urls import path
from recipes.views import home, contato, sobre, teste


urlpatterns = [
    path("home/", home),
    path('sobre/', sobre),
    path('contato/', contato),
    path('teste/', teste),
]

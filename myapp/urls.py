from django.urls import path
from myapp.views import website,home,about, contact


urlpatterns = [
    path("website/",website),
    path("website/home",home),
    path("website/about",about),
    path("website/contact",contact),
    
]
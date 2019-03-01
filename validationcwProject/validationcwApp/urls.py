from django.urls import path
from . import views

# routes set
urlpatterns = [
    # path("", views.newcars, name="newcars"),
    path("", views.index, name="index"),
]
from django.urls import path
from fruits import views

urlpatterns = [
    path("", views.home, name="home"),
    path("fruits/<name>", views.hello_there, name="hello_there"),
]
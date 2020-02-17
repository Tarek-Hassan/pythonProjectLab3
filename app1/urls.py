from django.urls import path
from app1 import views

urlpatterns = [
    path('index', views.index),
    path('home', views.home),
    path('age/<id>', views.age),
    path('showst/<id>', views.showStudent),
    path('addst', views.addStudent),
    path('editst/<id>', views.editStudent),
    path('delst/<id>', views.delStudent),

]








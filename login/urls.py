from django.urls import path
from login import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("dashView/",views.dashView,name="dashView"),
    path("",views.indexView,name="home"),
    path('login/',LoginView.as_view(),name="login"),
    path('register/',views.regesterView,name="register"),
    path('logout/',LogoutView.as_view(next_page="dashView"),name="logout")
]
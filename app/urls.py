from django.urls import path
from . import views
from django.views.generic import RedirectView
urlpatterns=[
    path("home/",views.home.as_view()),
    path("",RedirectView.as_view(url="home/")),
    path("login/",views.login_view.as_view()),
    path("logout/",views.logout_view.as_view()),
]
from operator import imod
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import logout
class home(View):
    def get(self, request, *args, **kwargs):
        return render(request,"home.html")

class login_view(View):
    def get(self, request, *args, **kwargs):
        return render(request,"accounts/login.html")

class logout_view(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/app/home/")

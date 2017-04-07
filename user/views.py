from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class Signup(View):
    def get(self, request):
        return render(request, "signup.html", {})

    def post(self, request):
        return self.get(request)

class Signin(View):
    def get(self, request):
        return render(request, "signin.html", {})

    def post(self, request):
        return self.get(request)

class Signout(View):
    @method_decorator(login_required(login_url='/signin/'))
    def get(self, request):
        return render(request, "signin.html", {})

# Create your views here.

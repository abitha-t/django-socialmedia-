from django.shortcuts import render
from . import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, logout


# Create your views here.
class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name='accounts/signup.html'
    def get_success_url(self):
      return reverse_lazy('login')

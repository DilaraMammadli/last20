from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import User, UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm

class UserRegisterView(generic.CreateView):
    model = User
    from_class=SignUpForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')
    # fields = '__all__'
    fields = ('username','first_name', 'last_name','password',)
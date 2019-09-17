from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Wish

def home(request):
    wishs = Wish.objects.all()
    return render(request, 'home.html', { 'wishs': wishs })
class WishCreate(CreateView):
    model = Wish
    fields = '__all__'
    success_url = '/'
class WishDelete(DeleteView):
    model = Wish
    success_url = '/'

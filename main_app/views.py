from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Todo


def todos_index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {"todos": todos})


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

class TodoCreate(CreateView):
  model = Todo
  fields = ['title', 'description','date', 'importance']
  success_url = '/todos/'

class TodoUpdate(UpdateView):
  model = Todo
  fields = ['description', 'date']
  success_url = '/todos/'

class TodoDelete(DeleteView):
  model = Todo
  success_url = '/todos/'


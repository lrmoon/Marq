from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import Todo


def todos_index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {"todos": todos})


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'



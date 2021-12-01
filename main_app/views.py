from django.shortcuts import render
from django.contrib.auth.views import LoginView



class Todo:  # Note that parens are optional if not inheriting from another class
  def __init__(self, title, desc, date, importance):
    self.title = title
    self.desc = desc
    self.date = date
    self.importance = importance

todos = [
  Todo('gym', 'go to gym', '01/04/2022.', "important"),
  Todo('swim', 'go to swimming', '01/07/2022', 'general'),
  Todo('band', 'go to band', '01/02/2042', 'minor'),
  Todo('Bank', 'go to  bank', '01/09/2022', 'minor')
]


def todos_index(request):
    return render(request, 'todos/index.html', {"todos": todos})


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'



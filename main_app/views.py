from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Event, Todo

class Home(LoginView):
    template_name = 'home.html'

######################1 todo code #########################
def todos_index(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/index.html', {"todos": todos})

class TodoCreate(CreateView):
  model = Todo
  fields = ['title', 'description','date', 'importance']
  success_url = '/todos/'

  def form_valid(self,form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TodoUpdate(UpdateView):
  model = Todo
  fields = ['title','description', 'date', 'importance']
  success_url = '/todos/'

class TodoDelete(DeleteView):
  model = Todo
  success_url = '/todos/'
  
######################## events code ##################################
def events_index(request):
  events = Event.objects.all()
  return render(request, 'events/index.html', {"events": events})

class EventCreate(CreateView):
  model = Event
  fields = '__all__'
  success_url = '/events/'

class EventUpdate(UpdateView):
  model = Event
  fields = '__all__'
  success_url = '/events/'

class EventDelete(DeleteView):
  model = Event
  success_url = '/events/'


######################## signup ##################################
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('todos_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)





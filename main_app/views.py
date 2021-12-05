from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta, date
from django.views import generic
import calendar
from .models import *
from .utils import Calendar
from .forms import EventForm


def todos_index(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/index.html', {"todos": todos})


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

class TodoCreate(CreateView):
  model = Todo
  fields = ['title', 'description','date', 'importance']
  success_url = '/todos/'

  def form_valid(self,form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class TodoUpdate(UpdateView):
  model = Todo
  fields = ['title', 'description','date', 'importance']
  success_url = '/todos/'

class TodoDelete(DeleteView):
  model = Todo
  success_url = '/todos/'
  

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


class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'cal/event.html', {'form': form})

class EventUpdate(UpdateView):
  model = Event
  instance = Event()
  fields = '__all__'
  success_url = '/calendar/'

def events_index(request):
  events = Event.objects.all()
  return render(request, 'events/index.html', {"events": events})

class EventDelete(DeleteView):
  model = Event
  success_url = '/events/'


# Timer Code


class TimerList(ListView):
    model = Timer
    template_name = 'timers/index.html'


class TimerDetail(DetailView):
    model = Timer
    template_name = 'timers/detail.html'

class TimerCreate(CreateView):
  model = Timer
  fields = '__all__'
  success_url = '/timers/'

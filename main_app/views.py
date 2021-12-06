from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'newmarq'



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



def add_photo(request, note_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  print(photo_file)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
		# uuid.uuid4().hex generates a random hexadecimal Universally Unique Identifier
    # Add on the file extension using photo_file.name[photo_file.name.rfind('.'):]
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to cat_id or cat (if you have a cat object)
      photo = Photo(url=url, note_id=note_id)
      # Remove old photo if it exists
      note_photo = Photo.objects.filter(note_id=note_id)
      if note_photo.first():
        note_photo.first().delete()
      photo.save()
      print(photo)
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('notes_update', pk=note_id)


def notes_index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {"notes": notes})

def notes_detail(request,note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'notes/detail.html', {'note':note})

class NoteUpdate(UpdateView):
    model = Note
    instance = Note()
    fields = '__all__'
    success_url = '/notes/'

class NoteDelete(DeleteView):
  model = Note
  success_url = '/notes/'


class NoteCreate(CreateView):
  model = Note
  fields = ['title', 'note','image', 'video']
  success_url = '/notes/'

  



from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('todos/', views.todos_index, name='todos_index'),
    path('todos/create/', views.TodoCreate.as_view(), name="todos_create"),
    path('todos/<int:pk>/update/', views.TodoUpdate.as_view(), name='todos_update'),
    path('todos/<int:pk>/delete/', views.TodoDelete.as_view(), name='todos_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('events/', views.events_index, name='events_index'),
    path('events/create/', views.event, name='event_new'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='event_edit'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),

    path('timers/', views.TimerList.as_view(), name='timers_index'),
    path('timers/<int:pk>/', views.TimerDetail.as_view(), name='timers_detail'),
    path('timers/create/', views.TimerCreate.as_view(), name="timers_create"),
    path('timers/<int:pk>/delete/', views.TimerDelete.as_view(), name='timers_delete'),

    path('notes/', views.notes_index, name='notes_index'),
    path('notes/create/', views.NoteCreate.as_view(), name="notes_create"),
    path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='notes_update'),
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='notes_delete'),
    path('notes/<int:note_id>/add_photo/', views.add_photo, name='add_photo'),

]


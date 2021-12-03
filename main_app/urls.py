from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('todos/', views.todos_index, name='todos_index'),
    path("todos/create/", views.TodoCreate.as_view(), name="todos_create"),
    path('todos/<int:pk>/update/', views.TodoUpdate.as_view(), name='todos_update'),
    path('todos/<int:pk>/delete/', views.TodoDelete.as_view(), name='todos_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('events/', views.events_index, name='events_index'),
    path('events/create/', views.event, name='event_new'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='event_edit'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
]


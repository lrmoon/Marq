from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    ########################3 Todo paths ##############################
    path('todos/', views.todos_index, name='todos_index'),
    path("todos/create/", views.TodoCreate.as_view(), name="todos_create"),
    path('todos/<int:pk>/update/', views.TodoUpdate.as_view(), name='todos_update'),
    path('todos/<int:pk>/delete/', views.TodoDelete.as_view(), name='todos_delete'),
    ########################3 Signup paths ##############################
    path('accounts/signup/', views.signup, name='signup'),
    ########################3 Event paths ##############################
    path('events/', views.events_index, name='events_index'),
    path("events/create/", views.EventCreate.as_view(), name="events_create"),
]


from django.urls import path

from . import views


app_name = 'routine'

urlpatterns = [
    path('create/', views.CreateRoutineView().as_view()),
    path('get/', views.RoutineView().as_view()),
    path('list/', views.RoutineListView().as_view())
]
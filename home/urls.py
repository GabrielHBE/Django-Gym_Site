from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    #tabs
    path('home/', views.home, name='home'),
    path('schedule/', views.schedule, name='schedule'),
    path('about/', views.about, name='about'),
    path('instructor/', views.instructors, name='instructor'),
    path('workout/', views.workout, name='workout'),  

    #funcs
    path('workout/start-workout/<int:id>/',views.start_workout,name='start_workout'),
    path('workout/finish-workout/',views.finish_workout,name='finish_workout'),

    #User
    path('user/register/', views.register, name='register'),
    path('user/update/<int:id>/', views.home, name='update'),
    path('user/delete/<int:id>/', views.home, name='delete'),
    path('user/login/', views.login, name='login'), 
    path('user/logout/',views.logout, name='logout'),

    #home_forms
    path('workout/add-workout/',views.add_workout,name='add_workout')
]

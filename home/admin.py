from django.contrib import admin
from home import models

# Register your models here.
@admin.register(models.UserParams)
class UserParamsAdmin(admin.ModelAdmin):

    list_display = ('id','gender', 'birth_date', 'objective', 'instructor')
    ordering = '-id',
    search_fields = ('id','email',)
    list_per_page = 10


@admin.register(models.Exercises)
class ExercisesAdmin(admin.ModelAdmin):

    list_display = ('id', 'name','duration', 'series', 'reps', 'workout')
    ordering = '-id',
    search_fields = ('id','name',)
    list_per_page = 10


@admin.register(models.Workout)
class WorkoutAdmin(admin.ModelAdmin):

    list_display = ('id', 'name','description', 'duration', 'user')
    ordering = 'id',
    search_fields = ('id','name',)
    list_per_page = 10


@admin.register(models.Instructor)
class instructorAdmin(admin.ModelAdmin):

    list_display = ('id', 'name','birth_date', 'gender', 'about')
    ordering = '-id',
    search_fields = ('id','name',)
    list_per_page = 10


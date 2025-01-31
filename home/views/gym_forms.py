from django.shortcuts import render,redirect # type: ignore
from home.forms import  ExerciseForm, WorkoutForm
from home.models import Workout,Exercises,UserParams
from django.forms.models import inlineformset_factory # type: ignore
from home.funcs import *


def add_workout(request,workout_id=None):

    user = UserParams.objects.filter(user_id=request.user.id).order_by('-user_id')

    request_user = request.user

    user_params = get_user_params(request_user)
    user_id = user_params.get('id')
    
    form = WorkoutForm()
    form_exercise_factory = inlineformset_factory(Workout,Exercises,form=ExerciseForm,extra=7)
    form_exercise = form_exercise_factory()

    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        form_exercise_factory = inlineformset_factory(Workout,Exercises,form=ExerciseForm)
        form_exercise = form_exercise_factory(request.POST)

        if form.is_valid() and form_exercise.is_valid():

            delete_workouts = Workout.objects.filter(user_id=user_id)
            user.current_workout = None

            user_set_null = UserParams.objects.get(user_id=request_user.id)
            user.current_workout = None
            user_set_null.save()

            for i in delete_workouts:
                i.delete()

            workout = form.save(commit=False)
            workout.user = user.first()
            workout.save()
            form_exercise.instance = workout
            form_exercise.save()

            return redirect('home:home')

    context = {
        'form': form,
        'form_exercise': form_exercise, 
        'title': 'Add workout',
        }

    return render(request,'home/home_forms/add_workout.html',context)

from django.shortcuts import render,redirect
from home.forms import  ExerciseForm, WorkoutForm
from home.models import Workout,Exercises,UserParams
from django.forms.models import inlineformset_factory


def add_workout(request,workout_id=None):

    user = UserParams.objects.filter(user_id=request.user.id).order_by('-user_id')

    
    form = WorkoutForm()
    form_exercise_factory = inlineformset_factory(Workout,Exercises,form=ExerciseForm,extra=3)
    form_exercise = form_exercise_factory()

    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        form_exercise_factory = inlineformset_factory(Workout,Exercises,form=ExerciseForm)
        form_exercise = form_exercise_factory(request.POST)

        if form.is_valid() and form_exercise.is_valid():
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

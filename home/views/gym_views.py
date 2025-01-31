from django.shortcuts import render,redirect,get_object_or_404
from home.models import *
from home.funcs import *

# Create your views here.
def home(request):

    if not request.user.is_authenticated:
        return redirect('home:login')
    
    user = request.user
    
    #User data
    user_params = get_user_params(user)

    user_workout = get_user_workout(user)
  
    if user_workout is not None:
        current_workout = get_today_workout(user_workout,user)

    context = {
        'title': 'Home',    
        'workout_of_the_day': current_workout.get('name'),
        'user_name': user.username,
        'user_email': user.email,
        'user_instructor': user_params.get('instructor'),
        'user_objective': user_params.get('objective'),
        'workout_id': current_workout.get('id')
    }

    return render(request, 'home/index.html',context)

def schedule(request):

    if not request.user.is_authenticated:
        return redirect('home:login')

    context = {
        'title': 'Schedule',
    }

    return render(request, 'home/schedule.html',context)

def about(request):

    if not request.user.is_authenticated:
        return redirect('home:login')

    context = {
        'title': 'About',
    }

    return render(request, 'home/about.html',context)

def instructors(request):

    if not request.user.is_authenticated:
        return redirect('home:login')

    context = {
        'title': 'Instructors',
    }

    return render(request, 'home/instructor.html',context)

def workout(request):

    if not request.user.is_authenticated:
        return redirect('home:login')
    
    user = request.user
    
    #User data
    user_params = get_user_params(user)
    
    user_workout = get_user_workout(user)

    if user_workout is not None:
        current_workout = get_today_workout(user_workout,user)

    context = {
        'workout_of_the_day': current_workout.get('name'),
        'title': 'Workout',
        'completed_trainings': user_params.get('completed_trainings'),
        'workout_id': current_workout.get('id')
    }

    return render(request, 'home/workout.html',context)

def start_workout(request,id):

    if not request.user.is_authenticated:
        return redirect('home:login')
    
    user_workout = get_object_or_404(Workout.objects,pk=id)

    exercises = user_workout.exercises.all()

    exercises_with_range = []
    for exercise in exercises:

        exercises_with_range.append({
            "name": exercise.name,
            "duration": exercise.duration,
            "reps": exercise.reps,
            "series": exercise.series,
            "series_range": range(exercise.series if exercise.series else 0),  # Garante que 0 séries não gera erro
        })

    context = {
        'title': f'Workout {user_workout}',
        'workout_name': user_workout,   
        'exercises': exercises_with_range,
    }

    return render(request, 'home/start_workout.html',context)

def finish_workout(request):

    user = request.user

    user_params = UserParams.objects.get(user_id=user.id)

    if user_params.completed_trainings is None:
        user_params.completed_trainings = 0

    user_params.completed_trainings +=1
    user_params.save()
    
    workout_list = get_user_workout(user)    
    current_workout = get_today_workout(workout_list,user)

    pos=0
    for i in range(len(workout_list)):
        if workout_list[i].get('name') == current_workout.get('name'):
            pos=i+1

    try: 
        user_params.current_workout=workout_list[pos].get('name')
    except:
        user_params.current_workout=workout_list[0].get('name')

    user_params.save()

    return redirect('home:workout')
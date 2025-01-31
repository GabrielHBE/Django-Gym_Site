from home.models import *

def get_user_params(user):

    user_params = UserParams.objects.filter(user_id=user.id)

    for i in user_params:
        instructor = i.instructor
        if instructor is None:
            instructor = 'No instructor in your account'
        gender = i.gender
        photo = i.photo
        birth_date = i.birth_date
        objective = i.objective
        if objective is None:
            objective = "Just playing arround"
        id = i.id
        current_workout = i.current_workout
        completed_trainings = i.completed_trainings
        if completed_trainings is None:
            completed_trainings = 0

    return {
        'instructor': instructor,
        'gender': gender,
        'photo': photo,
        'birth_date': birth_date,
        'objective': objective,
        'id': id,
        'current_workout': current_workout,
        'completed_trainings': completed_trainings
    }


def get_user_workout(user_):

    user_params = get_user_params(user_)

    user_workout = Workout.objects.filter(user_id=user_params.get('id')).order_by('id')


    workout_list = []

    name=None
    description = None
    dutarion = None
    user = None
    for i in user_workout:
        name = i.name
        if name is None:
            name = '?'
        description = i.description
        dutarion = i.duration
        user = i.user
        id = i.id

        workout_dict = {
            'name': name,
            'description': description,
            'duration': dutarion,
            'user': user,
            'id':id,
        }

        workout_list.append(workout_dict)

    return workout_list


def get_today_workout(workout_list,user):

    workout_list.sort(key=lambda x: x["name"])
    user_params = UserParams.objects.filter(user_id=user.id).order_by('id')
    for i in user_params:
        current_workout = i.current_workout


    if current_workout is None:
        try:
            current_workout = workout_list[0]
            name = current_workout.get('name')
            if name is None:
                name = '?'
            description = current_workout.get('description')
            dutarion = current_workout.get('duration')
            user_ = current_workout.get('user')
            id = current_workout.get('id')

            workout_dict = {
                'name': name,
                'description': description,
                'duration': dutarion,
                'user': user_,
                'id':id
            }
            return workout_dict
        
        except:
            return {
                'name': '----',
                'description': 'Error',
                'duration': 'Error',
                'user': 'Error',
                'id':None
            }

        
    for i in workout_list:
        if i.get('name') == current_workout:
            name = i.get('name')
            if name is None:
                name = '?'
            description = i.get('description')
            dutarion = i.get('duration')
            user_ = i.get('user')
            id = i.get('id')

            workout_dict = {
                'name': name,
                'description': description,
                'duration': dutarion,
                'user': user_,
                'id':id
            }
            return workout_dict
        
    return {
            'name': '----',
            'description': 'Error',
            'duration': 'Error',
            'user': 'Error',
            'id': None
        }
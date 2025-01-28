from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Instructor(models.Model):
    gender_choices = (
        ("F", "Female"),
        ("M", "Male"),
        ("?", "I'm weird"),
    )

    name = models.CharField(max_length=100,blank=True,null=True)
    birth_date = models.DateTimeField(default=datetime.now())
    gender = models.CharField(max_length=1, choices=gender_choices,blank=True,null=True)  # Limitando a 1 caractere
    about = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.name) if self.name else "Unnamed"


class UserParams(models.Model):
    gender_choices = (
        ("F", "Female"),
        ("M", "Male"),
        ("?", "I'm weird"),
    )
    
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_params",blank=True,null=True
    )  # Relacionamento 1:1 com o modelo User


    gender = models.CharField(max_length=1, choices=gender_choices,blank=True,null=True)
    birth_date = models.DateTimeField(blank=True,null=True)
    objective = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    instructor = models.OneToOneField(
        Instructor, null=True, blank=True, on_delete=models.SET_NULL
    )

    completed_trainings = models.IntegerField(blank=True,null=True)
    current_workout = models.CharField(blank=True,null=True,max_length=1)

    def __str__(self):
        return str(self.user.username) if self.user.username else "Unnamed"


class Workout(models.Model):

    workout_choices = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E"),
        ("F", "F"),
        ("G", "G"),
    )

    name = models.CharField(max_length=1,blank=True,null=True, choices=workout_choices)
    description = models.CharField(max_length=100, blank=True, null=True)
    duration = models.DurationField(blank=True,null=True)
    user = models.ForeignKey(
        UserParams, blank=True, null=True, on_delete=models.CASCADE, related_name="workouts"
    )  # Treinos pertencem a um usuário

    def __str__(self):
        return str(self.name) if self.name else "Unnamed"


class Exercises(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    duration = models.DurationField(blank=True, null=True)
    series = models.PositiveIntegerField(blank=True, null=True)
    reps = models.PositiveIntegerField(blank=True, null=True)

    workout = models.ForeignKey(
        Workout,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="exercises",
    )  # Exercícios pertencem a um treino

    def __str__(self):
        return str(self.name) if self.name else "Unnamed"
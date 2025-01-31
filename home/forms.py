from .models import *
from django import forms # type: ignore
from django.core.exceptions import ValidationError # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth.models import User # type: ignore

class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email',ValidationError('Já existe um usiario com esse email',code='invalid'))

        return email
    

class UserParamsForm(forms.ModelForm):

    class Meta: 
        model = UserParams
        fields = ('birth_date', 'gender', 'objective', 'photo',)
        widgets = {
            'photo': forms.FileInput(attrs={'accept': 'image/*'}),
        }


class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ('name','description','duration',)

    def clean(self):

        name = self.cleaned_data.get('name')

        if not name:
            self.add_error('name',ValidationError('Add a name to the workout'))

        return super().clean()


class ExerciseForm(forms.ModelForm):

    class Meta:
        models = Exercises
        fields = ('name','duration','series','reps',)

    def clean(self):

        name = self.cleaned_data.get('name')

        if not name:
            self.add_error('name',ValidationError('Add a name to the exercise'))

        return super().clean()

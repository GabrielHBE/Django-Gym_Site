from .models import *
from django import forms # type: ignore
from django.core.exceptions import ValidationError # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.forms.models import inlineformset_factory


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


class ExerciseForm(forms.ModelForm):

    class Meta:
        models = Exercises
        fields = ('name','duration','series','reps',)

from django.shortcuts import render,redirect # type: ignore
from home.forms import RegisterForm, UserParamsForm # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from django.contrib import auth # type: ignore
from django.contrib.auth import login as auth_login


def register(request):

    form = RegisterForm()
    user_params_form = UserParamsForm()   

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        user_params_form = UserParamsForm(request.POST)     

        if form.is_valid() and user_params_form.is_valid():
            user = form.save()
            
            new_user_params = user_params_form.save(commit=False)
            new_user_params.user = user
            new_user_params.completed_trainings = 0
            new_user_params.save()
            messages.success(request,'Usuário logado')
            return redirect('home:login')

    context = {
        'form': form,
        'user_params_form': user_params_form,
        'title': 'Register',
    }

    return render(request,'home/user_forms/register.html',context)

def login(request):
    form = AuthenticationForm(request, data=request.POST if request.method == 'POST' else None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Logado com sucesso')
            return redirect('home:home')

        messages.error(request, 'Erro ao realizar login')

    context = {
        'form': form,
        'title': 'login',
    }
    return render(request, 'home/user_forms/login.html', context)


def logout(request):

    auth.logout(request)

    return redirect('home:login')


def update(request):

    form = RegisterForm(instance=request.user)

    context = {
        'form': form,
        'title': 'Update User'
    }


    if request.method!='POST':
        return render(request,'home/user_forms/update.html',context)

    form = RegisterForm(data=request.POST, isinstance=request.user)

    if not form.is_valid():
        return render(request,'home/user_forms/update.html',context)
    
    form.save()

    return redirect('home:user_update')
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomCreationForm 

# Create your views here.


def register(request):
    
    variables = {
        'form':CustomCreationForm
    }

    if request.POST:
        
        form = CustomCreationForm(request.POST)

        if form.is_valid():
                
                form.save()
                variables['mensaje'] = "Usuario creado"
        else:
                variables['mensaje'] = "No se ha registrado el usuario"
                variables['form'] = form

    return render(request, 'accounts/register.html', variables)
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import RegisterationForm, Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

def register(request) :
    if request.method == 'POST' :
        form = RegisterationForm(request.POST)
        if form.is_valid() :
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            
            
            user = Account.objects.create_user(first_name=first_name, last_name=last_name,
                                               email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, "Registeration Successful")
            return redirect('register')
        
            
    else :
        form = RegisterationForm()
            
    context = {
        'form' : form,
    }
    return render(request, 'accounts/register.html', context)

def login(request) :
    if request.method == 'POST' :
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        
        
        if user is not None :
            auth.login(request, user)
            # messages.success(request, 'You are now logged in.')
            return redirect('home')
        else :
            messages.error(request, 'Invalid login credentials.')
            return redirect('login')
        
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request) :
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return render(request, 'accounts/login.html')

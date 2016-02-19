from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
    
# Register new users 
def register(request):
    
    if request.POST['password'] == request.POST['password_confirmation']:
       User.objects.create_user(request.POST['fl_name'], request.POST['email'], request.POST['password'])

    return login_view(request)

# Validate username and password and log user in
def login_view(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return redirect('/tasks', {"user" : user})
        else:
                return render(request, 'index.html', {"errors" : "User is not active"})
    else:
        print("entrou")
        myUserEmail =  User.objects.filter(email = email).first()
        print(myUserEmail)
        if myUserEmail is None:
            return render(request, 'index.html', {"errors" : "Invalid email"})
        else:
            return render(request, 'index.html', {"errors" : "Invalid password"})
    

def logout_view(request):
    logout(request)
    return redirect('/')
    
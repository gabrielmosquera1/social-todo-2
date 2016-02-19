from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
    
# Register new users 
def register(request):
    name = request.POST['fl_name']
    password = request.POST['password']
    email = request.POST['email']
    confirmation = request.POST['password_confirmation']
    
    if len(name) < 1 or len(name) > 50 or len(password) > 50 or len(password) < 1 or len(email) < 1 or len(email) > 50:
        return render(request, 'index.html', {'errors' : 'Invalid fields'})
    
    if password == confirmation:
        try:
            User.objects.create_user(username=email, first_name=name, password=password)
        except:
            return render(request, 'index.html', {"errors" : "Account with this email already exists!"})
    else:
        return render(request, 'index.html', {"errors" : "Invalid password"})
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
            # return render(request, 'tasks.html', {"user" : user})
            return redirect('/task/')
        else:
                return render(request, 'index.html', {"errors" : "User is not active"})
    else:
        myUserEmail =  User.objects.filter(username = email).first()
        print(myUserEmail)
        if myUserEmail is None:
            return render(request, 'index.html', {"errors" : "Invalid email"})
        else:
            return render(request, 'index.html', {"errors" : "Invalid password"})
    

def logout_view(request):
    logout(request)
    return redirect('/')
    
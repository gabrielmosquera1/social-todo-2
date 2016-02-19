from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
    
def register(request):
    # return render(request,
    # print request.POST['fl_name']
    if request.POST['password'] == request.POST['password_confirmation']:
       User.objects.create_user(request.POST['fl_name'], request.POST['email'], request.POST['password'])

    return login_view(request)
    
    
    
    # pass

def login_view(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return redirect('/tasks')
        else:
                return render(request, 'index.html', {"errors" : "User is not active"})
    else:
        # Return an 'invalid login' error message.
        # ...
        print("entrou")
        myUserEmail =  User.objects.filter(email = email).first()
        print(myUserEmail)
        # myUserPassword = User.objects.filter(password = password)
        if myUserEmail is None:
            return render(request, 'index.html', {"errors" : "Invalid email"})
        else:
            return render(request, 'index.html', {"errors" : "Invalid password"})
    
    # return redirect('/tasks')
    
    # pass

def logout_view(request):
    # logout(request)
    # render(request, '/')
    pass
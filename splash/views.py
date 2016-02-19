from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

# Start the program in the task page if the user is logged in or
# in the login/register page if the user cannot be authenticated
def index(request):
    if request.user.is_authenticated():
        return redirect('/task/')
    else:
        return render(request, "index.html")
    
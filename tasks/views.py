from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the tasks index.") 
    return render(request, "tasks.html", );
    
def say_whatsup(request):
    return HttpResponse("Hello, WHAT IS UP?")
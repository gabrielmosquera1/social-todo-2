from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Task, User
from django.db.models import Q

# Create your views here.
def index(request):
    tasks = Task.objects.filter(Q(owner=request.user) | Q(collaborators=request.user)).distinct()
    return render(request, 'tasks.html', {'tasks' : tasks})


def create(request):
    if request.user.is_authenticated():
        newTask = Task(
            owner = request.user,
            title = request.POST['title'],
            description = request.POST['description'],
            isComplete = False,
            )
        
        newTask.save()
        collaborator1 = request.POST['collaborator1']
        col1 = User.objects.filter(username=collaborator1).first()
        print col1
        
        collaborator2 = request.POST['collaborator2']
        col2 = User.objects.filter(username=collaborator2).first()
        print col2
        
        collaborator3 = request.POST['collaborator3']
        col3 = User.objects.filter(username=collaborator3).first()
        print col3
        
        if col1 is not None:
            newTask.collaborators.add(col1)
        if col2 is not None:
            newTask.collaborators.add(col2)
        if col3 is not None:
            newTask.collaborators.add(col3)
        
        # newTask.save()
        
        return redirect('/task/')
    
    else:
        return render(request, "index.html", {"errors" : "User is not authenticated"});
    
def remove(request):
    Task.objects.filter(id=request.POST['taskId']).delete()
    
    return redirect('/task/')
    
def complete(request):
    print("complete!")
    task = Task.objects.filter(id=request.POST['taskId']).first()
    if task.isComplete == True:
        task.isComplete = False;
    else:
        task.isComplete = True
    task.save()
    
    return redirect('/task/')

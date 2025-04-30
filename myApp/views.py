from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProjects
# Create your views here.

def index(request):
    title = 'Django course'
    return render(request,'index.html', {'title':title})

def hello(request, username):
    return HttpResponse("hello world %s" % username)

def about(request):
    username = 'kibu'
    return render(request,"about.html",{'username':username})

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects':projects})

def tasks(request):
    #task= Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html',{'tasks':tasks})
    

def create_task(request):
    if request.method =='GET':
        return render(request, 'tasks/create_task.html',{
            'form':CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['Title'],description=request.POST['description'], project_id=2)
        return redirect('/tasks/')
    
def create_project(request):
    if request.method =='GET':
        return render(request, 'projects/create_project.html',{'form':CreateNewProjects()
         })
    else:
        Project.objects.create(name=request.POST["name"])
        redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })
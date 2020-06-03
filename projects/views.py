from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.views.generic.edit import FormView
from .forms import ProjectForm, FileProjectFormreport
from .models import Project, project_report
from article.models import Article
from events.models import Event
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def projects(request):
    keyword = request.GET.get("keyword")

    if keyword:
        projects = Project.objects.filter(title__contains=keyword)
        return render(request, "projects.html", {"projects": projects})
    projects = Project.objects.all()

    return render(request, "projects.html", {"projects": projects})

def proposed(request):
    keyword = request.GET.get("keyword")

    if keyword:
        projects = Project.objects.filter(title__contains=keyword)
        return render(request, "projects.html", {"projects": projects})
    projects = Project.objects.filter(status = '0')

    return render(request, "projects.html", {"projects": projects})

def in_pipeline(request):
    keyword = request.GET.get("keyword")

    if keyword:
        projects = Project.objects.filter(title__contains=keyword)
        return render(request, "projects.html", {"projects": projects})
    projects = Project.objects.filter(status = '1')

    return render(request, "projects.html", {"projects": projects})

def completed(request):
    keyword = request.GET.get("keyword")

    if keyword:
        projects = Project.objects.filter(title__contains=keyword)
        return render(request, "projects.html", {"projects": projects})
    projects = Project.objects.filter(status = '2')

    return render(request, "projects.html", {"projects": projects})

def executed(request):
    keyword = request.GET.get("keyword")

    if keyword:
        projects = Project.objects.filter(title__contains=keyword)
        return render(request, "projects.html", {"projects": projects})
    projects = Project.objects.filter(status = '3')

    return render(request, "projects.html", {"projects": projects})

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def register(request):
    return(request, "register.html")

@login_required(login_url="user:login")
def dashboard(request):
    projects = Project.objects.filter(author=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "dashboard.html", context)

@login_required(login_url="user:login")
def addProject(request):
    form = ProjectForm(request.POST or None)
    file_form = FileProjectFormreport(request.POST or None, request.FILES or None)
    reports = request.FILES.getlist('Project_report')

    if form.is_valid() and file_form.is_valid():
        project = form.save(commit=False)
        project.author = request.user
        project.save()
        for report in reports:
            Projectreport_instance = project_report(Project_report = report, Project = project)
            Projectreport_instance.save()

        messages.success(request, "Project Created Successfully!!!")
        return redirect("article:dashboard")

    return render(request, "addproject.html", {"form": form , "file_form": file_form})


def detail(request, id):
    #project = Project.objects.filter(id = id).first()
    project = get_object_or_404(Project, id=id)
    reports = project_report.objects.filter(project = project)

    return render(request, "project_detail.html", {"projects": project, "reports" : reports})

@login_required(login_url="user:login")
def updateProject(request, id):
    project = get_object_or_404(Project, id=id)
    form = ProjectForm(request.POST or None)
    file_form = FileProjectFormreport(request.POST, request.FILES)
    reports = request.FILES.getlist('Project_report')

    if form.is_valid() and file_form.is_valid():
        project = form.save(commit=False)
        project.author = request.user
        project.save()
        for report in reports:
            Projectreport_instance = project_report(Project_report = report, Project=project)
            Projectreport_instance.save()

        messages.success(request, "Project Created Successfully!!!")
        return redirect("article:dashboard")

    return render(request, "addproject.html", {"form": form , "file_form": file_form})

@login_required(login_url="user:login")
def deleteProject(request, id):
    project = get_object_or_404(Project, id=id)

    project.delete()

    messages.success(request, "Project Successfully Deleted")

    return redirect("article:dashboard")




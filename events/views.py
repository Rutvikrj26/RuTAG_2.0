from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import EventForm
from .models import Event
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from article.models import Article
from projects.models import Project

# Create your views here.

def events(request):
    keyword = request.GET.get("keyword")

    if keyword:
        events = Event.objects.filter(title__contains=keyword)
        return render(request, "events.html", {"events": events})
    events = Event.objects.all()

    return render(request, "events.html", {"events": events})

def workshop(request):
    keyword = request.GET.get("keyword")

    if keyword:
        events = Event.objects.filter(title__contains=keyword)
        return render(request, "events.html", {"events": events})
    events = Event.objects.filter(Event_type = 'Workshop')

    return render(request, "events.html", {"events": events})

def cgm(request):
    keyword = request.GET.get("keyword")

    if keyword:
        events = Event.objects.filter(title__contains=keyword)
        return render(request, "events.html", {"events": events})
    events = Event.objects.filter(Event_type = 'Core Group Meeting')

    return render(request, "events.html", {"events": events})

def cm(request):
    keyword = request.GET.get("keyword")

    if keyword:
        events = Event.objects.filter(title__contains=keyword)
        return render(request, "events.html", {"events": events})
    events = Event.objects.filter(Event_type = 'Club Meeting')

    return render(request, "events.html", {"events": events})

def spm(request):
    keyword = request.GET.get("keyword")

    if keyword:
        events = Event.objects.filter(title__contains=keyword)
        return render(request, "events.html", {"events": events})
    events = Event.objects.filter(Event_type = 'Staff & PI Meetings')

    return render(request, "events.html", {"events": events})

def other(request):
    keyword = request.GET.get("keyword")

    if keyword:
        events = Event.objects.filter(title__contains=keyword)
        return render(request, "events.html", {"events": events})
    events = Event.objects.filter(Event_type = 'other Events')

    return render(request, "events.html", {"events": events})


def index(request):
    return render(request, "index.html")

def register(request):
    return(request, "register.html")

@login_required(login_url="user:login")
def dashboard(request):
    projects = Project.objects.filter(author=request.user)
    events = Event.objects.filter(author=request.user)
    articles = Article.objects.filter(author=request.user)
    context = {
        "projects": projects,
        "article" : articles,
        "events" : events
    }
    return render(request, "dashboard.html", context)

@login_required(login_url="user:login")
def addEvent(request):
    form = EventForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        event = form.save(commit=False)


        messages.success(request, "Event Created Successfully!!!")
        return redirect("events:dashboard")
    return render(request, "addevent.html", {"form": form})


def detail(request, id):
    #event = Event.objects.filter(id = id).first()
    event = get_object_or_404(Event, id=id)


@login_required(login_url="user:login")
def updateEvent(request, id):
    event = get_object_or_404(Event, id=id)
    form = EventForm(request.POST or None, request.FILES or None, instance=event)
    if form.is_valid():
        event = form.save(commit=False)

        messages.success(request, "Event Successfully Updated")
        return redirect("events:dashboard")

    return render(request, "update.html", {"form": form})


@login_required(login_url="user:login")
def deleteEvent(request, id):
    event = get_object_or_404(Event, id=id)

    event.delete()

    messages.success(request, "Event Successfully Deleted")

    return redirect("events:dashboard")




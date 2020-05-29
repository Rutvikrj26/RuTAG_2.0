from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import EventForm
from .models import Event
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def events(request):
    keyword = request.GET.get("keyword")

    if keyword:
        events = Event.objects.filter(title__contains=keyword)
        return render(request, "events.html", {"events": events})
    events = Event.objects.all()

    return render(request, "events.html", {"events": events})


def index(request):
    return render(request, "index.html")

def register(request):
    return(request, "register.html")

@login_required(login_url="user:login")
def dashboard(request):
    events = Event.objects.filter(author=request.user)
    context = {
        "events": events
    }
    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def addEvent(request):
    form = EventForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        event = form.save(commit=False)


        messages.success(request, "Event Created Successfully!!!")
        return redirect("event:dashboard")
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
        return redirect("event:dashboard")

    return render(request, "update.html", {"form": form})


@login_required(login_url="user:login")
def deleteEvent(request, id):
    event = get_object_or_404(Event, id=id)

    event.delete()

    messages.success(request, "Event Successfully Deleted")

    return redirect("event:dashboard")




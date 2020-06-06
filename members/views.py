from django.shortcuts import render, redirect, reverse
from .models import contact, Member, news, writeup, publication


def members(request):
    member = Member.objects.all()
    return render(request, "members.html", {"members": member})

def core(request):
    member = Member.objects.filter(work = '0').order_by('-level')
    return render(request, "members.html", {"members": member})

def club(request):
    member = Member.objects.filter(work = '1').order_by('-level')

    return render(request, "club.html", {"members": member})

def about(request):
    News = news.objects.all().order_by('-date')
    Writeup = writeup.objects.all()

    return render(request, "about.html", {"news" : News, "writeup" : Writeup})

def contactpage(request):
    contacts = contact.objects.all()
    return render(request, "contact.html", {"contacts" : contacts})

def publications(request):
    Publications = publication.objects.all().order_by('-date')
    return render(request, "Publications.html", {"publications" : Publications})

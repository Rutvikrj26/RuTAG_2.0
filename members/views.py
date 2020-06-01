from django.shortcuts import render, redirect, reverse
from .models import contact, Member
from .forms import contactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage

def contactpage(request):
    form = contactForm(request.POST or None)
    if form.is_valid():
        contact_name = request.POST.get(
            'name'
            , '')
        contact_email = request.POST.get(
            'email'
            , '')
        form_content = request.POST.get('query', '')
        template = get_template('contact_template.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        }
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "Your website" + '',
            ['rutag@iitd.ac.in'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return redirect('contact')
    return render(request, 'contact.html', {'form': form})

def core(request):
    members = Member.objects.filter(position__contains = "RuTAG Club")
    return render(request, "members.html", {"members": members})

def club(request):
    members = Member.objects.filter(position__contains = "Core")
    return render(request, "members.html", {"members": members})

from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
def home(request):
    if request.method=="POST":
        contact = Contact()
        subject=request.POST.get('subject')
        email = request.POST.get('email')
        text = request.POST.get('subject')

        contact.subject = subject
        contact.email = email
        contact.text = text
        contact.save()

        return HttpResponse("<h1> THANKS FOR CONTACT ME </h1>")

    return render(request, 'base/index.html')

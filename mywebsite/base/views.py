from django.shortcuts import render
from .models import Contact

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


        return render(request, 'base/messsent.html')

    return render(request, 'base/index.html')


def error_404(request, exception):
    return render(request, 'base/404.html')
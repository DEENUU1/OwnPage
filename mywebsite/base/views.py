from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def home(request):
    return render(request, 'base/index.html')


def contact_view(request):
    form = ContactForm()
    context = {'form': form}
    return HttpResponse(request, 'base/templates/base/index.html', context)



# Create your views here.

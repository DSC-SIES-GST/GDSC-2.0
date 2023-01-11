from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    faqs = Faq.objects.filter(is_live=True)
    print(faqs)
    context = {
        'faqs' : faqs
    }
    return render(request, 'contact/faq.html', context)
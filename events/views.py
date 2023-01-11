from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
  events = models.Event.objects.order_by('-date').filter(is_live=True)
  print(events)
  context = {
      'events' : events
  }
  return render(request, 'events/events.html', context)
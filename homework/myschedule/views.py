from django.shortcuts import render
from .models import Schedule

# Create your views here.
def home(request):
    schedule = Schedule.objects
    return render(request, 'schedule/home.html', {'sch':schedule})
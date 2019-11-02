from django.shortcuts import render
from .models import Job


def home(request):
    jobs = Job.objects.all().order_by('-pub_date')
    return render(request, 'jobs/home.html', {'jobs':jobs})

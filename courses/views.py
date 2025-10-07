from django.shortcuts import render
from .models import Sector

def course_list(request):
    sectors = Sector.objects.prefetch_related("subjects__courses").all()
    return render(request, "courses/course_list.html", {"sectors": sectors})

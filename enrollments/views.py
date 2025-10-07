from django.shortcuts import render
from .models import Enrollment

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, "enrollments/enrollment_list.html", {"enrollments": enrollments})

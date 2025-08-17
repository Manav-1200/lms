from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.views.generic import ListView
from .models import Course

class CourseListView(ListView):
    """
    Students can search courses by name, instructor, or difficulty.
    Paginated list (10 per page by default via settings).
    """
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"

    def get_queryset(self):
        qs = Course.objects.select_related("instructor").filter(is_active=True)
        q = self.request.GET.get("q", "").strip()
        difficulty = self.request.GET.get("difficulty", "").strip()
        if q:
            qs = qs.filter(
                Q(title__icontains=q)
                | Q(description__icontains=q)
                | Q(instructor__username__icontains=q)
                | Q(instructor__first_name__icontains=q)
                | Q(instructor__last_name__icontains=q)
            )
        if difficulty:
            qs = qs.filter(difficulty=difficulty)
        return qs

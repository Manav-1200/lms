from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def sponsor_dashboard(request):
    return render(request, "sponsors/sponsor_dashboard.html")

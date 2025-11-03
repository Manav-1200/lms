from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Sponsorship

@login_required
def sponsor_list(request):
    # list sponsorships for the logged-in user (sponsors see their sponsorships)
    items = Sponsorship.objects.filter(sponsor=request.user)
    return render(request, "sponsors/list.html", {"items": items})

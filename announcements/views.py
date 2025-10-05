from django.shortcuts import get_object_or_404, render
from .models import Announcement

# Create your views here.
def home(request):
    context = {
        'title': 'Home Page', 
        'features': [
            'Django', 
            'Templates', 
            'Static Files'
        ],
    }
    return render(request, 'home.html', context)

def announcement_list(request):
    # ✅ Always define the variable
    announcements = Announcement.objects.all()
    return render(
        request,
        "announcements/announcements.html",
        {"announcements": announcements}
    )

def detail(request, id):
    announcement = get_object_or_404(Announcement, pk=id)
    return render(
        request,
        "announcements/detail.html",
        {"announcement": announcement}
    )
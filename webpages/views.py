from django.shortcuts import render
from django.http import HttpResponse
from .models import Slider, Team
from youtubers.models import Youtuber


# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    team_members = Team.objects.all()
    featured_youtuber = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'sliders': sliders,
        'team_members': team_members,
        'featured_youtuber': featured_youtuber,
        'tubers': tubers
    }
    return render(request, 'webpages/home.html', data)


def about(request):
    return render(request, 'webpages/about.html')


def service(request):
    return render(request, 'webpages/service.html')


def contact(request):
    return render(request, 'webpages/contact.html')

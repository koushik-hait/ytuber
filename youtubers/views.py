from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Youtuber


# Create your views here.
def youtubers(request):
    ytrs = Youtuber.objects.order_by('-created_date')
    data = {
        'ytrs': ytrs,
    }
    return render(request, 'youtubers/youtuber.html', data)


def search(request):
    tubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search = Youtuber.objects.values_list('camera', flat=True).distinct()
    catagory_search = Youtuber.objects.values_list('catagory', flat=True).distinct()

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            tubers = tubers.filter(description__icontains=keywords)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
    if 'camera' in request.GET:
        camera = request.GET['camera']
        if camera:
            tubers = tubers.filter(camera__iexact=camera)
    if 'catagory' in request.GET:
        catagory = request.GET['catagory']
        if catagory:
            tubers = tubers.filter(catagory__iexact=catagory)
    data = {
        'tubers': tubers,
        'city_search': city_search,
        'camera_search': camera_search,
        'catagory_search': catagory_search,
    }
    return render(request, 'youtubers/search.html', data)


def youtubers_detail(request, id):
    ytdt = get_object_or_404(Youtuber, pk=id)
    data = {
        'ytdt': ytdt,
    }
    return render(request, 'youtubers/youtubers_detail.html', data)

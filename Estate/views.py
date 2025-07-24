from django.shortcuts import render
from .models import *

def index_view(request):
    categories = Category.objects.all()
    estates = Estate.objects.all()
    return render(request, 'mainPages/index.html', context={'categories':categories, 'estates':estates })

def detail_view(request,estate_id):
    similar_estates = Estate.objects.filter(category=Estate.objects.get(id=estate_id).category)
    estate = Estate.objects.get(id=estate_id)
    return render(request, 'mainPages/work-single.html', context={'estate':estate, 'similar_estates':similar_estates})

def about_view(request):
    return render(request, 'mainPages/about.html')


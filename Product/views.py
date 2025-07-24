from django.shortcuts import render
from .models import *

def index_view(request):
    categories = Category.objects.all()
    estates = Estate.objects.all()
    return render(request, 'mainPages/index.html', context={'categories':categories, 'estates':estates })

def detail_view(request,estate_id):
    estate = Estate.objects.get(id=estate_id)
    return render(request, 'mainPages/detail.html', context={'estate':estate})

from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def index_view(request):
    parent_categories = Category.objects.filter(parent_category__isnull=True)
    estates = Estate.objects.all()
    return render(request, 'mainPages/index.html', context={'parent_categories':parent_categories, 'estates':estates })

def detail_view(request,estate_id):
    similar_estates = Estate.objects.filter(category=Estate.objects.get(id=estate_id).category)
    estate = Estate.objects.get(id=estate_id)
    return render(request, 'mainPages/work-single.html', context={'estate':estate, 'similar_estates':similar_estates})

def about_view(request):
    return render(request, 'mainPages/about.html')

def filter_cards_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    estates = Estate.objects.filter(category=category, is_active=True)
    return render(request, 'mainPages/filtered_cards_page.html', {
        'category': category,
        'estates': estates,
    })

def user_favourite_estates(request, estate_id):
    like_exists = Favourite.objects.filter(user=request.user, estate=estate_id).exists()
    estate = get_object_or_404(Estate, id=estate_id)

    if not like_exists:
        like = Favourite(
            user=request.user,
            estate=estate,
        )
        like.save()
    if like_exists:
        like = Favourite.objects.get(user=request.user, estate=estate_id)
        like.delete()

    return render(request, 'mainPages/favourite_estates.html')


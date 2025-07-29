from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def index_view(request):
    parent_categories = Category.objects.filter(parent_category__isnull=True)
    estates = Estate.objects.filter(is_active=True)  # Only active estates
    liked_estates = []

    if request.user.is_authenticated:
        liked_estates = Favourite.objects.filter(user=request.user).values_list('estate_id', flat=True)

    return render(request, 'mainPages/index.html', context={
        'parent_categories': parent_categories,
        'estates': estates,
        'liked_estates': liked_estates
    })

def detail_view(request,estate_id):
    similar_estates = Estate.objects.filter(category=Estate.objects.get(id=estate_id).category)
    estate = Estate.objects.get(id=estate_id)
    return render(request, 'mainPages/work-single.html', context={'estate':estate, 'similar_estates':similar_estates})

def about_view(request):
    return render(request, 'mainPages/about.html')

def filter_cards_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    estates = Estate.objects.filter(category=category, is_active=True)
    liked_estates = []
    if request.user.is_authenticated:
        liked_estates = Favourite.objects.filter(user=request.user).values_list('estate_id', flat=True)
    return render(request, 'mainPages/filtered_cards_page.html', {
        'category': category,
        'estates': estates,
        'liked_estates': liked_estates
    })

def user_favourite_estates(request, estate_id):
    if not request.user.is_authenticated:
        return redirect('login')

    like_exists = Favourite.objects.filter(user=request.user, estate=estate_id)
    estate = get_object_or_404(Estate, id=estate_id)

    if not like_exists:
        like = Favourite(
            user=request.user,
            estate=estate,
        )
        like.save()
    else:
        like_exists.delete()

    next_page = request.GET.get('next')
    if next_page == 'favourites':
        return redirect('user_favourite_estates_filter')
    elif next_page == 'filtered_cards':
        category_id = request.GET.get('category_id')
        if category_id:
            return redirect('filtered_cards', category_id=category_id)
    return redirect('index')

def user_favourite_estates_filter(request):
    if not request.user.is_authenticated:
        return redirect('login')

    favourite_estates = Favourite.objects.filter(user=request.user)
    return render(request, 'mainPages/favourites.html', {'favourite_estates': favourite_estates})

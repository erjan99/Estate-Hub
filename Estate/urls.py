from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', index_view, name='index'),
  path('detail_view/<int:estate_id>/', detail_view, name='detail_view'),
  path('about/', about_view, name='about'),
  path('filtered_cards/<int:category_id>/', filter_cards_by_category, name='filtered_cards'),
  path('favourite/<int:estate_id>/', user_favourite_estates, name='user_favourite_estates'),
  path('favourites/', user_favourite_estates_filter, name='user_favourite_estates_filter'),
  path('feedback/<int:estate_id>/', user_feedback, name='user_feedback'),
  path('delete_feedback/<int:feedback_id>/', feedback_deletion, name='delete_feedback')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
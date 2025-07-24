from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index_view, name='index'),
    path('detail_view/<int:estate_id>/', detail_view, name='detail_view')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

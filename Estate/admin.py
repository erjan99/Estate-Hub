from django.contrib import admin
from .models import Category, Estate, City, District, Image,Favourite

class EstateAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'city', 'district', 'price', 'is_active')
    list_filter = ('category', 'city', 'district', 'is_active')
    search_fields = ('name', 'description')


admin.site.register(Category)
admin.site.register(Estate, EstateAdmin)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Image)
admin.site.register(Favourite)

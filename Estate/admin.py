from django.contrib import admin
from .models import *

class EstateAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'city', 'district')
    list_filter = ('category', 'city', 'district')
    search_fields = ('title', 'description')

admin.site.register(Estate)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Image)



# Register your models here.

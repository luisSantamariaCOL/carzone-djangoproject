from django.contrib import admin
from .models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html(f'<img src="{object.main_photo.url}" width="40" style="border-radius: 50px" />')
    
    thumbnail.short_description = 'Car Image'

    list_display = ("id", "thumbnail", "title", "city", "color", "model", "year", "body_style", "fuel_type", "price", "is_featured")
    list_display_links = ('id', 'thumbnail', 'title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'title', 'city', 'model', 'body_style', 'fuel_type')

    list_filter = ('city', 'model', 'body_style', 'fuel_type')

# Register your models here.
admin.site.register(Car, CarAdmin)
from django.contrib import admin
from models import *
from django.contrib.contenttypes import generic

class ImageInline(admin.StackedInline):
    model = SentenceImage
    
class OrderImageInline(admin.TabularInline):
    model = OrderImage    
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'user', 'born', 'city')
    list_filter = ['born', 'user', 'city']
    search_fields = ['title']
    inlines = [OrderImageInline, ]

class SentenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'user', 'born', 'city')
    list_filter = ['born', 'user', 'city']
    search_fields = ['title']
    inlines = [ImageInline, ]
    
class ImageCompanyInline(admin.StackedInline):
    model = CompanyImage

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'city')
    list_filter = ['user', 'city']
    search_fields = ['title']
    inlines = [ImageCompanyInline, ]
    
class CityAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']

    
admin.site.register(Page)
admin.site.register(Order, OrderAdmin)
admin.site.register(Sentence, SentenceAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Category)
admin.site.register(Subcategory)
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
    

    
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title','parent')
    search_fields = ['title']
    list_filter = ['parent']
    
class SubsubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title','parent')
    search_fields = ['title']
    list_filter = ['parent']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('my_order','title')
    list_editable = ('my_order',)


    
admin.site.register(Page)
admin.site.register(Order, OrderAdmin)
admin.site.register(Sentence, SentenceAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Subcategory,SubcategoryAdmin)
admin.site.register(Subsubcategory, SubsubcategoryAdmin)
admin.site.register(BlockInfo)
admin.site.register(BlockonPage)
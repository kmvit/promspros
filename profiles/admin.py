from django.contrib import admin
from models import UserProfile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'phone')
# Register your models here.
admin.site.register(UserProfile,ProfileAdmin)

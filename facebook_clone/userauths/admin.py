from django.contrib import admin
from userauths.models import User, Profile

# create class inherits from models.py
# list_display will be displayed on User and Profile screens
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'username', 'email', 'gender']
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'user', 'verified']
    list_editable = ['verified']
    
#register on actual site
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
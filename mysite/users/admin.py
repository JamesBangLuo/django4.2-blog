from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.unregister(User)
class UserProfileInline(admin.StackedInline):
    model = UserProfile
class userAdmin(UserAdmin):
    inlines = [UserProfileInline]
admin.site.register(User,userAdmin)
from django.contrib import admin
from .models import CustomUser,CustomUserProfile
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", ]

    


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUserProfile)
# admin.site.register(Follower)

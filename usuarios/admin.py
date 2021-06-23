from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import UserProfile

@admin.register(UserProfile)
class UserAdmin(auth_admin.UserAdmin):
    list_filter = ('perfil',)
    form = UserChangeForm
    add_form = UserCreationForm
    model = UserProfile
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos personalizados", {"fields": ("empresa","foto","perfil",)}),
    )


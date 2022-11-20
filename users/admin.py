from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['uuid', 'first_name', 'email']
    fieldsets = (
        (None, {'fields' : ('username', 'password')}),
        ('Informacion Personal', {'fields' : ('first_name', 'last_name', 'email')}),
        ('Permisos', {'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('others', {'fields': ('gender', 'date_birthday')}),
    )
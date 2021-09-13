from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import *
from .forms import RegisterForm
# Register your models here.


@admin.register(CustomUser)
class UserAdmin(DjangoUserAdmin):
    form = RegisterForm
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Personal Details'), {'fields': ('mobile_number',)}),
        (_('Invitations'), {'fields': ('invite_query', 'invited_by',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name',
                    'invited_by', 'invite_query', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

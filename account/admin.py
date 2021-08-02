from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Account
from .forms import UserAdminChangeForm, UserAdminCreationForm

admin.site.unregister(Group)


class AccountAdmin(UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = ['username', 'email', 'staff']
    list_filter = ['username']
    readonly_fields = ['admin']
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Permissions', {
            'fields': ('staff', 'admin'),
        }),
    )
    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('username', 'email', 'password', 'password_2')
    }), )
    search_fields = ['username']
    ordering = ['username']
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)
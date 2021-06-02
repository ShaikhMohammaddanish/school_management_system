from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class AccountAdmin(UserAdmin):
    list_display = ('email', 'user_name', 'date_joined','last_login', 'is_admin', 'is_superuser', 'user_type', 'Contact_no', 'Gender', 'Address', 'City', 'State' ,'Country','image'  )
    search_fields = ('email', 'user_name',  'user_type', 'Contact_no','Address', 'City', 'State')
    readonly_fields = ('date_joined','last_login', 'is_admin', 'is_superuser')
    filter_horizontal =()
    list_filter = ('user_type',)
    ordering = ('email',)
    fieldsets=()

    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    # )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )





   
    



# Register your models here.
admin.site.register(models.userProfile, AccountAdmin)
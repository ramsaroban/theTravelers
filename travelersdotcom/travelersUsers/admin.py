from django.contrib import admin
from .models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ['id','email','first_name','last_name','user_type','is_admin']
    search_field = ['email','user_type']

admin.site.register(Users, UsersAdmin)

# Register your models here.

from django.contrib import admin
from restful_api.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('_id', 'password', 'name')


admin.site.register(User, UserAdmin)
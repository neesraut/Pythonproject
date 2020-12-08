from django.contrib import admin
from .models import Users

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','updated_at','created_at')


# Register your models here.
admin.site.register(Users,UserAdmin)



from django.contrib import admin
from .models import studentRegistration
# Register your models here.



class studentadmin(admin.ModelAdmin):
    list_display=('username','first_name','Last_name','email','password',)

admin.site.register(studentRegistration ,studentadmin)

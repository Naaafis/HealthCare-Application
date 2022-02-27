from django.contrib import admin

# Register your models here.
from .models import Device, User, Data_Collection

admin.site.register(Device)
admin.site.register(User)
admin.site.register(Data_Collection)
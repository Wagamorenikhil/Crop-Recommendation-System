from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Season, Crop,Admin,User

admin.site.register(Season)
admin.site.register(Crop)
admin.site.register(Admin)
admin.site.register(User)

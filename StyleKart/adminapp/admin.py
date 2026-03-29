from django.contrib import admin
from .models import user_registration,product
# Register your models here.

admin.site.register(user_registration)
admin.site.register(product)

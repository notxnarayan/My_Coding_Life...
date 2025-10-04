from django.contrib import admin
from .models import CustomUser, category,Product
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(category)
admin.site.register(Product)

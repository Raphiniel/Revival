from django.contrib import admin
from .models import Category, Blog, Description

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Description)
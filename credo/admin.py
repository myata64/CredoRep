from django.contrib import admin
from .models import UserProfile, Product


@admin.register(UserProfile)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class CourseAdmin(admin.ModelAdmin):
    pass

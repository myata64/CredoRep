from django.contrib import admin
from .models import UserProfile, Category, Product
from .forms import UserProfileForm, CategoryForm, ProductForm


@admin.register(UserProfile)
class PersonAdmin(admin.ModelAdmin):
    form = UserProfileForm
    pass


@admin.register(Product)
class CourseAdmin(admin.ModelAdmin):
    form = ProductForm
    pass


@admin.register(Category)
class CourseCategory(admin.ModelAdmin):
    form = CategoryForm
    pass

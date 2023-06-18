from django.contrib import admin
from .models import Category, Product
from .forms import CategoryForm, ProductForm


@admin.register(Product)
class CourseAdmin(admin.ModelAdmin):
    form = ProductForm
    pass


@admin.register(Category)
class CourseCategory(admin.ModelAdmin):
    form = CategoryForm
    pass

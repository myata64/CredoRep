from django.contrib import admin
from .models import User, Category, Product
from .forms import UserForm, CategoryForm, ProductForm


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('username', 'email', 'phone_number',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
    pass


@admin.register(Product)
class CourseAdmin(admin.ModelAdmin):
    form = ProductForm
    pass


@admin.register(Category)
class CourseCategory(admin.ModelAdmin):
    form = CategoryForm
    pass

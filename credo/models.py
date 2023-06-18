from django.db import models


# Пользователь
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


# Товары

class Category(models.Model):
    name_category = models.CharField(max_length=100)

    def __str__(self):
        return self.name_category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_product = models.CharField(max_length=100)
    model = models.CharField(max_length=100, default='')
    size = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    availability = models.BooleanField(default=True)
    description = models.TextField(default=0)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name_product

# class Cart(models.Model):
#     user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
#     product

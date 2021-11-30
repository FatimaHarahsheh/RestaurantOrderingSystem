from django.db import models

class Employee(models.Model):
    username=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Qrcode(models.Model):
    qrimage=models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Invoice(models.Model):
    tableNumber=models.CharField(max_length=225)
    total=models.FloatField(max_length=225)
    orderDetailes=models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order (models.Model):
    tableNumber=models.IntegerField(max_length=225)
    quntity=models.FloatField(max_length=225)
    numberOfinvoice=models.IntegerField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    invoice = models.ForeignKey(Invoice, related_name="orders", on_delete = models.CASCADE)


class Category(models.Model):
    mealType=models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Meal(models.Model):
    mealName=models.CharField(max_length=225)
    price=models.FloatField(max_length=225)
    description=models.CharField(max_length=225)
    mealImage=models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(Order, related_name="meals", on_delete = models.CASCADE)
    category = models.ForeignKey(Category, related_name="categorymeals", on_delete = models.CASCADE) 
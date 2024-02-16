from django.db import models
from django.contrib.auth.models import AbstractUser


class Store(AbstractUser) :
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Store'

class Menu(models.Model):
    menuId = models.BigAutoField(primary_key=True)
    storeId = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    optionId = models.ManyToManyField('Option')
    price = models.IntegerField()
    menuImgUrl = models.TextField(null=True, blank=True)
    status = models.IntegerField(max_length=1, default=1)
    #options = models.ManyToManyField('Option', through='MenuOption', related_name='menus')

    def __str__(self):
        return f'{self.name}'

class Option(models.Model):
    optionId = models.BigAutoField(primary_key=True)
    #menuId = models.ForeignKey(Menu, on_delete=models.CASCADE)
    option = models.CharField(max_length=255)
    contents = models.ManyToManyField('OptionContent', null=True, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField(max_length=5, default=1)
    status = models.IntegerField(max_length=1, default=1)

    #menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    #menu_option = models.ManyToManyField(Menu)

    def __str__(self):
        return f'{self.option}'

class OptionContent(models.Model):
    content = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.content}'

class Cart(models.Model):
    cartId = models.BigAutoField(primary_key=True)
    menuId = models.ForeignKey(Menu, on_delete=models.CASCADE)
    optionId = models.ForeignKey(Option, on_delete=models.CASCADE)
    type = models.IntegerField(max_length=1)

class Order(models.Model):
    orderId = models.BigAutoField(primary_key=True)
    menuId = models.ForeignKey(Menu, on_delete=models.CASCADE)
    optionId = models.ForeignKey(Option, on_delete=models.CASCADE)
    pay = models.CharField(max_length=255)
    totalPrice = models.IntegerField()
    totalQuantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)

# class MenuOption(models.Model):
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
#     option = models.ForeignKey(Option, on_delete=models.CASCADE)
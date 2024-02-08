from django.contrib import admin
from .models import Store, Menu, Option, OptionContent, Cart, Order

admin.site.register(Store)
admin.site.register(Menu)
admin.site.register(Option)
admin.site.register(OptionContent)
admin.site.register(Cart)
admin.site.register(Order)

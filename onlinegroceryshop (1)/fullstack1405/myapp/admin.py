from django.contrib import admin
from .models import Userdata,Product,Cart,Payment

# Register your models here.
admin.site.register(Userdata)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Payment)

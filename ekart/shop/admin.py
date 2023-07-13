from django.contrib import admin
from .models import Category
from .models import Product

class CatergoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description')
admin.site.register(Category,CatergoryAdmin)
admin.site.register(Product)


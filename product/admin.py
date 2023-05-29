from django.contrib import admin
from product.models import Product,Comment
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'created_date', 'modified_date')
    sortable_by = ('id', 'name', 'category', 'created_date', 'modified_date')


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)

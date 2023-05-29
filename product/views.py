from django.shortcuts import render
from product.models import Product

# Create your views here.


def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id_):
    if request.method == 'GET':
        product = Product.objects.get(id=id_)
        context = {
            'product': product,
            'comments': product.comment_set.all()
        }
        return render(request, 'products/detail.html', context=context)

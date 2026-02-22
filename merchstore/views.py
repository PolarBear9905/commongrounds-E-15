from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product

def product_list(request):
    products = Product.objects.all()
    ctx = {"products": products}
    return render(request, "merchstore/product_list.html", ctx)

def product_detail(request, pk):
    ctx = {"merchstore": Product.objects.get(id=pk)}
    return render(request, "merchstore/product_detail.html", ctx) 

class ProductListView(ListView):
    model = Product
    template_name = "merchstore/product_list.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = "merchstore/product_detail.html"
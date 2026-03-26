from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product, Transaction

def index(request):
    return redirect('items/')

class ProductListView(ListView):
    model = Product
    template_name = "merchstore/product_list.html"
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            user_products = Product.objects.filter(owner=self.request.user.profile)
            all_products = Product.objects.exclude(owner=self.request.user.profile)
        else:
            user_products = []
            all_products = Product.objects.all()

        context['user_products'] = user_products
        context['all_products'] = all_products
        return context
    

class ProductDetailView(DetailView):
    model = Product
    template_name = "merchstore/product_detail.html"



class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "merchstore/product_create.html"
    fields = ['name', 'product_type', 'product_image', 'description', 'price', 'stock', 'status']

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "merchstore/product_update.html"
    fields = ['name', 'product_type', 'product_image', 'description', 'price', 'stock', 'status']


class CartView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "merchstore/cart_view.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.filter(buyer=self.reuqest.user.profile).get_queryset()

class TransactionsListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "merchstore/transaction_list.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.filter(product_owner=self.reuqest.user.profile).get_queryset()


from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from rest_framework import viewsets

from common.views import TitleMixin
from products.models import Basket, Product, ProductCategory

from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'

    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data()
    #     context['title'] = 'Store'
    #     return context


# def index(request):
#     context = {'title': 'Store'}
#     return render(request, 'products/index.html', context)


class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = "Store - Каталог"

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        # context['title'] = "Store - Каталог"
        context['categories'] = ProductCategory.objects.all()
        return context


# def products(request, category_id=None, page=1):
#     context = {'title': 'Store - Каталог', 'categories': ProductCategory.objects.all()}
#     if category_id:
#         products = Product.objects.filter(category_id=category_id)
#     else:
#         products = Product.objects.all()
#     paginator = Paginator(products, 3)
#     products_paginator = paginator.page(page)
#     context.update({'products': products_paginator})
#     return render(request, 'products/products.html', context)


@login_required(login_url='/users/login')
def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)


@login_required(login_url='/users/login')
def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

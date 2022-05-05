from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Product
from django.views import generic
# Create your views here.


class IndexPage(generic.TemplateView):
    template_name = "index.html"


class ProductListView(generic.ListView):
    template_name = 'product_list.html'
    paginate_by = 20
    model = Product
    queryset = Product.objects.filter(is_active=True)
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product
    context_object_name = 'product'     # стандартный это object
    # slug_field = 'id'
    # slug_url_kwarg = 'pk'     # под капотом DetailView сам вытаскивает pk

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from category.models import Category
from product.forms import ProductForm
from product.models import Product


def start_view(reguest):
    return render(reguest, 'product/start.html')


class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 4


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = self.request.GET.get('page')
        return context

    def get_queryset(self, queryset=None):
        search = self.request.GET.get('search')
        queryset = super().get_queryset()
        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'product/create.html'
    success_url = reverse_lazy('list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'category', 'price', 'image', 'slug']
    template_name = 'product/update.html'
    success_url = reverse_lazy('list')
    context_object_name = "product"



class ProductDeleteView(DeleteView):
    model = Product
    fields = '__all__'
    template_name = 'product/delete.html'
    success_url = reverse_lazy('list')

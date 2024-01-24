from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from category.forms import CategoryForm
from category.models import Category
from product.models import Product



class CategoryListView(ListView):
    model = Category
    template_name = 'category/cat_list.html'
    context_object_name = 'categories'
    paginate_by = 10


    def get_queryset(self, queryset=None):
        search = self.request.GET.get('search')
        queryset = super().get_queryset()
        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'category/detail_list_cat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['products'] = Product.objects.filter(category=category)
        context['current_page'] = self.request.GET.get('page')
        return context

class CategoryCreateView(CreateView):
    form_class = CategoryForm
    template_name = 'category/create_cat.html'
    success_url = reverse_lazy('cat_list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_page'] = self.request.GET.get('page')
        return context

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'slug']
    template_name = 'category/update_cat.html'
    success_url = reverse_lazy('cat_list')
    context_object_name = "category"



class CategoryDeleteView(DeleteView):
    model = Category
    fields = '__all__'
    template_name = 'category/delete_cat.html'
    success_url = reverse_lazy('cat_list')

from django.urls import path

from category.views import CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryListView, \
    CategoryDeleteView

urlpatterns = [
    path('cat_list/', CategoryListView.as_view(), name='cat_list'),
    path('list_cat/<slug:slug>/', CategoryDetailView.as_view(), name='list_cat'),
    path('create_cat/', CategoryCreateView.as_view(), name='create_cat'),
    path('update_cat/<slug:slug>', CategoryUpdateView.as_view(), name='update_cat'),
    path('delete_cat/<slug:slug>', CategoryDeleteView.as_view(), name='delete_cat'),
]
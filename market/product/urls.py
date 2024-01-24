from django.urls import path

from product.views import start_view, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

urlpatterns = [
    path('', start_view, name='start'),
    path('list/', ProductListView.as_view(), name='list'),
    path('detail/<slug:slug>', ProductDetailView.as_view(), name='detail'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
]
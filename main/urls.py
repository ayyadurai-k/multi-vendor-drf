from django.urls import path
from main.views import VendorList,VendorDetail,ProductList,ProductDetail


urlpatterns = [
    path('vendors/',VendorList.as_view(),name="list_vendors"),
    path('vendor/<int:pk>/',VendorDetail.as_view(),name="detail_vendor"),
    path('products/',ProductList.as_view(),name="list_products"),
    path('product/<int:pk>/',ProductDetail.as_view(),name="detail_product"),
]
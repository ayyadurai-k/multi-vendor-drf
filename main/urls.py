from django.urls import path
from main.views import VendorList,VendorDetail,CustomerAddressViewSet,ProductRatingViewSet,ProductList,ProductDetail,CustomerList,CustomerDetail,OrderList,OrderDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router = SimpleRouter() #DOESN'T PROVIDES APIs
router.register('address',CustomerAddressViewSet)
router.register('product-rating',ProductRatingViewSet)

urlpatterns = [
    path('vendors/',VendorList.as_view(),name="list_vendors"),
    path('vendor/<int:pk>/',VendorDetail.as_view(),name="detail_vendor"),
    path('products/',ProductList.as_view(),name="list_products"),
    path('product/<int:pk>/',ProductDetail.as_view(),name="detail_product"),
    path('customers/',CustomerList.as_view(),name="list_customers"),
    path('customer/<int:pk>/',CustomerDetail.as_view(),name="detail_customer"),
    path('orders/',OrderList.as_view(),name="list_orders"),
    path('order/<int:pk>/',OrderDetail.as_view(),name="detail_order"),
]

urlpatterns += router.urls
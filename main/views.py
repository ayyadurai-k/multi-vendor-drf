from main.serializers import VendorSerializer,ProductSerializer,ProductDetailSerializer,ProductRatingSerializer,CustomerAddressSerializer,CustomerSerializer,OrderSerializer,OrderDetailSerializer
from rest_framework import generics
from main.models import Vendor,Product,Customer,Order,CustomerAddress,ProductRating
from main.pagination import CustomPagination
from rest_framework.viewsets import ModelViewSet

class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
    def perform_create(self, serializer):
        # Set the user field to the current authenticated user
        serializer.save(user=self.request.user)
    
class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    
    
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderDetail(generics.ListAPIView):
    # queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    
    
    def get_queryset(self):
        order_id = self.kwargs["pk"]
        order = Order.objects.get(id=order_id)
        order_items = order.order_items
        return order_items
    
class CustomerAddressViewSet(ModelViewSet):
    serializer_class = CustomerAddressSerializer
    queryset = CustomerAddress.objects.all()
    
    
class ProductRatingViewSet(ModelViewSet):
    serializer_class = ProductRatingSerializer
    queryset = ProductRating.objects.all()
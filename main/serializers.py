from rest_framework import serializers
from main.models import Vendor,Product,Customer,Order,OrderItems,CustomerAddress,ProductRating

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        super(VendorSerializer,self).__init__(*args,**kwargs)
        # self.Meta.depth = 1
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        super(ProductSerializer,self).__init__(*args,**kwargs)
        # self.Meta.depth = 2
        
class ProductDetailSerializer(serializers.ModelSerializer):
    ratings = serializers.StringRelatedField(many=True,read_only=True) #ATTRIBUTE NAME SAME AS RELATED_NAME 
    
    class Meta:
        model = Product
        fields = ["id","title","detail","price","category","vendor","ratings"]
        
    
    def __init__(self,*args,**kwargs):
        super(ProductDetailSerializer,self).__init__(*args,**kwargs)
        # self.Meta.depth = 2
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
    
    
class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        super(OrderDetailSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1
        
class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        super(CustomerAddressSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        super(ProductRatingSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1

        

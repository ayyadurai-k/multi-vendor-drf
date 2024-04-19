from rest_framework import serializers
from main.models import Vendor,Product

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        super(VendorSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        super(ProductSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 2
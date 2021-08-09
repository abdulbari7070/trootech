from rest_framework import serializers 
from categories.models import Product, Category
 

# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


# class SubCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubCategory
#         fields = '__all__'
#     lookup_field = 'id_parent'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','parent')
 
class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=True, read_only=True)
    # category = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ('title','description','price','category')
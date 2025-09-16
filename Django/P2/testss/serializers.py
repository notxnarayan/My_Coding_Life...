from rest_framework import serializers

from testss.models import category,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Use the nested serializer for category
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializer1(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.categoryname", read_only=True)
    category_des = serializers.CharField(source="category.description", read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
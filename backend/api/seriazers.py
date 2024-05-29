from rest_framework import serializers


class UserProductSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    price = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)


class ProductUserSerializer(serializers.Serializer):
    related_products = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(read_only=True)
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)


    def get_related_products(self, obj):
        qs = obj.product_set.all()
        return UserProductSerializer(qs, many=True).data[:2]

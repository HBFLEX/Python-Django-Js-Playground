from rest_framework import serializers
from rest_framework.reverse import reverse
from api.seriazers import ProductUserSerializer
from .validators import validate_title

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # title_bizarre = serializers.SerializerMethodField()
    owner = ProductUserSerializer(source='user')
    url = serializers.SerializerMethodField()
    edit_url = serializers.HyperlinkedIdentityField(view_name='product-edit', lookup_field='pk')
    title = serializers.CharField(validators=[validate_title])
    class Meta:
        model = Product
        fields = ['owner','id', 'edit_url', 'url', 'title', 'description', 'price', 'calculate_discount']

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-detail', kwargs={'pk': obj.pk}, request=request)
    
    # def get_user(self, obj):
    #     user = obj.user
    #     user_data = {}

    #     user_data['username'] = user.username
    #     user_data['id'] = user.id

    #     return user_data
    

    # def validate_title(self, value):
    #     product = Product.objects.filter(title__iexact=value)
    #     if product.exists():
    #         raise serializers.ValidationError('Product already added')
    #     return value

    # def get_title_bizarre(self, obj):
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.title

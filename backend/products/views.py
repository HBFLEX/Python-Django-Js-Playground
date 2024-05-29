from rest_framework import generics, mixins, permissions, authentication
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_queryset(self, *args, **kwargs):
        # user = self.request.user
        # qs = super().get_queryset(*args, **kwargs)
        # if user is None:
        #     return qs
        # return qs.filter(user=user)
        return super().get_queryset(*args, **kwargs)


    def perform_create(self, serializer):
        user = self.request.user
        if user is None:
            return None
        return serializer.save(user=user)


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def perform_create(self, serializer):
        if self.request.data['description'] is None or '':
            serializer.save(description=self.request.data['title'])

@api_view(['GET', 'POST'])
def alt_view(request, pk=None, *args, **kwargs):

    if request.method == 'GET':
        if pk is not None:
            products = Product.objects.filter(pk=pk).first()
            serializer_data = ProductSerializer(products)
            return Response(serializer_data.data, status=200)

        products = Product.objects.all()
        serializer_data = ProductSerializer(products, many=True).data

        return Response(data=serializer_data)
        
    if request.method == 'POST':
        product_data = ProductSerializer(data=request.data)

        if product_data.is_valid(raise_exception=True):
            product_data.save()
            return Response(data=product_data.data, status=201)

    return Response(product_data.errors, status=400) 




class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get(self, request, *args, **kwargs):
        if kwargs['pk'] is not None:
            return self.retrieve(request, args, kwargs)
        return self.list(request, *args, **kwargs)
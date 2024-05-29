from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer
from django.db.models import Q
from products import client


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
        print("this gets saved too")
    return Response(serializer.errors, status=400)


# class SearchApiView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


#     def get_queryset(self, *args, **kwargs):
#         qs = super().get_queryset(*args, **kwargs)
#         query = self.request.GET.get('q')

#         if query is not None:
#             lookup = Q(title__icontains=query) | Q(description__icontains=query) | Q(user__username__icontains=query)
#             qs = qs.filter(lookup).filter(public=True)
#         else:
#             qs = qs.filter(title=None)

#         return qs



class SearchApiView(generics.GenericAPIView):
    def get(self, *args, **kwargs):
        query = self.request.GET.get('query')
        tag = self.request.GET.get('tag') or None
        if query is None:
            return Response(data='', status=400)
        results = client.perfom_search(query, tags=tag)
        return Response(data=results, status=200)



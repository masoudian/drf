from rest_framework import authentication, generics, permissions

from api.authentication import *

from .models import Product
from .serializers import ProductSerializer

from .permissions import IsStaffPermission

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [  ### don't need it here anymore as we have it in settings now
    #     authentication.SessionAuthentication,
    #     TokenAuthentication # for header as 'Bearer'
    #     # authentication.TokenAuthentication   # for header as default ('Token')
    # ]
    permission_classes = [permissions.IsAdminUser, IsStaffPermission]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title + ' - content'
        serializer.save(content = content)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffPermission]


class ProductUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffPermission]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffPermission]

    def perform_destroy(self, instance):
        ## instance ...
        return super().perform_destroy(instance)



# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
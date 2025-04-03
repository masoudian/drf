import json
from django.forms import model_to_dict
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request, *args, **kwargs): # this is django HttpRequest
    # drf api view
    instance = Product.objects.all().order_by('?').first()
    data ={}
    if instance:
        # # data['id'] = instance.id
        # # data['title'] = instance.title
        # data = model_to_dict(instance, fields=['id', 'content', 'sale_price'])
        data = ProductSerializer(instance).data

    return Response(data)
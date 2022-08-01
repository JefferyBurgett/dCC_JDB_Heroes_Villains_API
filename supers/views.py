from django.shortcuts import get_object_or_404 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from super_types.models import SuperType
from super_types.serializers import SuperTypeSerializer
from .serializers import SuperSerializer
from .models import Super
# Create your views here.
@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET':

        super_type = request.query_params.get('type')
        queryset = Super.objects.all()
        if super_type:
            queryset = queryset.filter(super_type__type=super_type)

        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Custom Dictionary Response
@api_view(['GET'])
def supers_and_supertypes(request):
    # if request.method == 'GET':

    heroes = Super.objects.all()
    villains = Super.objects.all()

    heroes_serializer = SuperSerializer(heroes, many=True)
    villains_serializer = SuperSerializer(villains, many=True)

    custom_response_dict = {
    'Heroes': heroes_serializer.data,
    'Villains': villains_serializer.data
    }

    return Response(custom_response_dict)   
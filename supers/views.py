from django.shortcuts import get_object_or_404 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
# Create your views here.
@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET':
        queryset = Super.objects.all()
        supers = Super.objects.all()
        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    serializer = SuperSerializer(super)
    return Response(serializer.data)
    

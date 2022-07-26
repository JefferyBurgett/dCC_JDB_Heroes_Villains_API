from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Super
# Create your views here.
@api_view(['GET'])
def supers_list(request):
    supers = Super.objects.all()
    serializer = SuperSerializer(supers, many=True)
    return Response('ok')
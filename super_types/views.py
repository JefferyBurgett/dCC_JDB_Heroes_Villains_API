from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperTypeSerializer
from .models import SuperType

@api_view(['GET'])
def super_types_list(request):
    if request.method == 'GET':

        super_type = request.query_params.get('type')
        print(super_type)
        queryset = SuperType.objects.all()
        # supers = SuperType.objects.all()
        serializer = SuperTypeSerializer(queryset, many=True)
        return Response(serializer.data)


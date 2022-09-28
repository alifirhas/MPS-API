from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import TingkatAktivitas
from base.model_filter import TingkatAktivitasFilter
from api.serializers.TingkatAktivitasSerializer import TingkatAktivitasSerializer


@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        try:
            queryset = TingkatAktivitas.objects.all()
            filterset = TingkatAktivitasFilter(request.GET, queryset=queryset)
            
            if filterset.is_valid():
                queryset = filterset.qs
                
            serializer = TingkatAktivitasSerializer(queryset, many=True)

            return Response({
                "message": "Berhasil mengambil tingkat aktivitas",
                "statusCode": 200,
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "Terjadi masalah",
                "statusCode": 400,
                "error": e.args[0]
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def show(request, id):
    if request.method == 'GET':
        try:
            aktivitas = TingkatAktivitas.objects.get(id=id)
            serializer = TingkatAktivitasSerializer(aktivitas, many=False)

            return Response({
                "message": "Berhasil mengambil tingkat aktivitas",
                "statusCode": 200,
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "Terjadi masalah",
                "statusCode": 400,
                "error": e.args[0]
            }, status=status.HTTP_400_BAD_REQUEST)

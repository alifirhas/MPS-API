from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import User, UserProfile
from api.serializers.UserSerializer import UserSerializer, UserProfileSerializer


@api_view(["GET"])
def show(request, id):
    if request.method == "GET":
        try:
            user_queryset = User.objects.exclude(is_staff=1).get(id=id)
            profile_queryset = UserProfile.objects.get(user_id = id)
            
            user_serializer = UserSerializer(user_queryset, many=False)
            profile_serializer = UserProfileSerializer(profile_queryset, many=False)

            return Response({
                "message": "Berhasil mengambil User",
                "statusCode": 200,
                "data": {**user_serializer.data, **profile_serializer.data}
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "Terjadi masalah",
                "statusCode": 400,
                "error": e.args[0]
            }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update(request, id):
    if request.method == "PUT":
        body = request.data
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user, data = body)

            if serializer.is_valid():
                serializer.save()

            return Response({
                "message": "Berhasil update user",
                "statusCode": 200,
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "Terjadi masalah",
                "statusCode": 400,
                "error": e.args[0]
            }, status=status.HTTP_400_BAD_REQUEST)
            
@api_view(["DELETE"])
def destroy(request, id):
    if request.method == "DELETE":
        try:
            user = User.objects.get(id=id)
            user.delete()

            return Response({
                "message": "Berhasil hapus user",
                "statusCode": 200,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "Terjadi masalah",
                "statusCode": 400,
                "error": e.args[0]
            }, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterSerializer


# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "status": "OK",
                "message": "User Created Successfully."
            })
        else:
            return Response({"status": "error", "message": serializer._errors})
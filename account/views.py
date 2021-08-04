from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken


# Logout API
class LogoutApi(generics.GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        try:
            refresh_token = RefreshToken(request.data['refresh'])
            refresh_token.blacklist()

            return Response({'status': 'ok'},
                            status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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
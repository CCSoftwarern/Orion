
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


# Create your views here.

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'last_name': user.last_name,
            'first_name': user.first_name,
            'last_login': user.last_login,
            'is_staff': user.is_staff,
            'is_active': user.is_active

        })
    

class AuthExampleAPIView(APIView):
    authentication_classes = (BasicAuthentication, )

    def get(self, request, format=None):
        content = {
            'user': str(request.user)
        }
        return Response(content)

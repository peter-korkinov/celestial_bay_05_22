from rest_framework import generics
from rest_framework.permissions import AllowAny

from my_auth.models import MyUser
from my_auth.serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

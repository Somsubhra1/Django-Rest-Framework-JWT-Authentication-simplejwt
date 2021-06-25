from accounts.serializers import UserSerializer
from rest_framework import generics, permissions

# Create your views here.


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

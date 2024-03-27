from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.


class TodoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter the queryset to include only todo items of the current user
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user field to the current authenticated user
        serializer.save(user=self.request.user)
    
class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter the queryset to include only todo items of the current user
        return Todo.objects.filter(user=self.request.user)
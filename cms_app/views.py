from requests import Response
from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from .models import User, Like, Post
from .serializers import UserSerializer, LikeSerializer, PostSerializer
from .permissions import IsOwner, IsOwnerOrPublic


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]  # Use Token-based authentication
    permission_classes = [IsOwner]
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrPublic | IsOwner]

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [TokenAuthentication]  # Use Token-based authentication
    permission_classes = [IsOwner]

def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
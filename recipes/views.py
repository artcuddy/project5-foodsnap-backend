from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from foodsnap_api.permissions import IsOwnerOrReadOnly
from .models import Recipe
from .serializers import RecipeSerializer, RecipeDetailSerializer


class RecipeList(generics.ListCreateAPIView):
    """
    List recipes or create a recipe if logged in.
    """
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipe.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a recipe, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RecipeDetailSerializer
    queryset = Recipe.objects.all()

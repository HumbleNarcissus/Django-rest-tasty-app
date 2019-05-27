from rest_framework import viewsets, permissions
from . import models
from . import serializers
from .permissions import IsOwner

class RecipeViewset(viewsets.ModelViewSet):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        return models.Recipe.objects.filter(owner=user)
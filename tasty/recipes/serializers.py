from rest_framework import serializers
from . import models

class RecipeSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = models.Recipe
        fields = ('title', 'description', 'directions', 'ingredients', 'owner')
from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'trainer', 'name', 'description', 'created_at')
        model = Pokemon
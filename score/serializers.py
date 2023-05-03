from rest_framework import serializers

from .models import Player, Score


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'uuid', 'username', 'max_score']


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['url', 'score', 'player']

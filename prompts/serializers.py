from rest_framework import serializers
from .models import Prompt, Vote

class PromptSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Prompt
        fields = [
            "id",
            "author",
            "prompt",
            "tags",
            "votes",
            "expected_output"
        ]

    def get_author(self, obj):
        return obj.author.username

    def get_votes(self, obj):
        v = list(x.value for x in obj.votes.all())
        sum_ = sum(v)
        return sum_

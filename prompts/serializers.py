from rest_framework import serializers
from .models import Prompt

class PromptSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Prompt
        fields = [
            "id",
            "author",
            "prompt",
            "tags",
            "expected_output"
        ]

    def get_author(self, obj):
        return obj.author.username

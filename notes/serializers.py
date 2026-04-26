from rest_framework import serializers
from .models import Note, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class NoteSerializer(serializers.ModelSerializer):
    # This lets us see the actual tag names instead of just ID numbers
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        # --- ADDED 'priority' AND 'is_done' TO THIS LIST ---
        fields = ["id", "text", "tags", "priority", "is_done", "created_at", "updated_at"]
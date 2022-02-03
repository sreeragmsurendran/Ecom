from curses import meta
from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import Note
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
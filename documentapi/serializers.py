from rest_framework import serializers
from documentapi.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('documentId', 'category', 'creator',  'owner', 'file_name')

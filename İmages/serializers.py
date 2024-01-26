from rest_framework import serializers
from İmages.models import Image

base_str="http://127.0.0.1:8000/files/"

class ImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Image
        fields = ("id", "name", "url", "type", "size", "image")

    def get_url(self, obj):
        url = base_str + ""+str(obj.img)
        return url
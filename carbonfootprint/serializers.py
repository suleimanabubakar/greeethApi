from rest_framework.serializers import Serializer,ModelSerializer,StringRelatedField
from .models import *


class FootPrintSerializer(ModelSerializer):
    user = StringRelatedField(read_only=True)
    class Meta:
        model = UserFootPrint
        fields = '__all__'
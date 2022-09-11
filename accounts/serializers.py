from rest_framework.serializers import ModelSerializer,StringRelatedField
from .models import *

class ProfileSerializer(ModelSerializer):
    user = StringRelatedField(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'





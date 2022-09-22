from rest_framework.serializers import ModelSerializer,StringRelatedField
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','total_trees_planted','total_footprint','total_points','total_offset']

class ProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'





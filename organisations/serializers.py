from .models import *
from rest_framework.serializers import *

class OrganisationSerializer(ModelSerializer):
    created_by = StringRelatedField(read_only=True)

    class Meta:
        model = Organisation
        fields = '__all__'


class OrganisationUserSerializer(ModelSerializer):
    user = StringRelatedField(read_only=True)
    class Meta:
        model = OrganisationOfficial
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields=  '__all__'
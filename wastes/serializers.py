from rest_framework.serializers import ModelSerializer,StringRelatedField,SerializerMethodField
from .models import *


class WasteTypeSerializer(ModelSerializer):
    class Meta:
        model = WasteType
        fields = '__all__'


class WasteSerializer(ModelSerializer):
    owner = StringRelatedField(read_only=True)

    class Meta:
        model = RecycleWaste
        fields = '__all__'


class BidWasteSerializer(ModelSerializer):
    owner = StringRelatedField(read_only=True)
    waste_details = SerializerMethodField(read_only=True)
    class Meta:
        model = WasteBid
        fields = '__all__'

    def get_waste_details(self,bid):
        return WasteSerializer(bid.waste).data


class BidStatusChangeSerializer(ModelSerializer):
    class Meta:
        model = WasteBid
        fields = ['status',]
    

class SaleWasteSerializer(ModelSerializer):
    class Meta:
        model = SoldWaste
        fields = '__all__'
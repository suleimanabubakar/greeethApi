from rest_framework import serializers

from maintainance.serializers import MaintainanceSerializer
from .models import *
from weather.serializers import *
class TreeSerializer(serializers.ModelSerializer):
    planter = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Tree
        fields = ['id','planter','created_on','location','height','image','tree_type','age','to_be_maintained']
        extra_kwargs = {
            'planter':{'write_only':True},
            'location':{'write_only':True},
            'image':{'write_only':True},
            'tree_type':{'write_only':True},
        }



class RetreiveTreeSerializer(serializers.ModelSerializer):
    maintainances = MaintainanceSerializer(many=True)
    weather = serializers.SerializerMethodField()

    def get_weather(self,tree):
        return tree.weather if tree.weather == "N/A" else CheckWeatherSerailizer(tree.weather).data
    class Meta:
        model = Tree
        fields = ['id','planter','created_on','location','height','image','to_be_maintained','tree_type','age','address','maintainances','weather']



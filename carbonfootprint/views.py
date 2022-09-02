from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from carbonfootprint.models import UserFootPrint

from carbonfootprint.serializers import FootPrintSerializer
# Create your views here.



class CarbonFootPrintLC(ListCreateAPIView):
    serializer_class = FootPrintSerializer
    

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return self.request.user.footprints.all()
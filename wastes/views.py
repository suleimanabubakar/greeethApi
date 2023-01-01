from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView,ListCreateAPIView,UpdateAPIView

# Create your views here.


class WasteTypesList(ListAPIView):
    serializer_class = WasteTypeSerializer
    queryset = WasteType.objects.all()



class CreateWaste(ListCreateAPIView):
    serializer_class = WasteSerializer
    queryset = RecycleWaste.objects.exclude(status='sold')


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)



class BidWaste(ListCreateAPIView):
    serializer_class = BidWasteSerializer
    queryset = WasteBid.objects.filter(status__in=['accepted','pending'])

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class BidStatusUpdate(UpdateAPIView):
    serializer_class = BidStatusChangeSerializer
    queryset = WasteBid.objects.all()


class SaleWaste(ListCreateAPIView):
    serializer_class = SaleWasteSerializer
    queryset = SoldWaste.objects.all()
    
    


class PendingWaste(ListAPIView):
    serializer_class = WasteSerializer
    queryset = RecycleWaste.objects.filter(status="pending")
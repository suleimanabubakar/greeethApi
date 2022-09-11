from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *
# Create your views here.


class OrganisationCreate(CreateAPIView):
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    

class AddOrganisationUser(CreateAPIView):
    serializer_class = OrganisationUserSerializer
    queryset = OrganisationOfficial.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class Categories(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

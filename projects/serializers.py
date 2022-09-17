
from rest_framework import serializers
from .models import *
from rest_framework.response import Response
from rest_framework import status
from organisations.serializers import OrganisationSerializer


class ProjectOrganisatiionSerailizer(serializers.ModelSerializer):
    class Meta:
        model = OrganisationInProject
        fields = '__all__'
        read_only_fields = ['project']


class AddOrganisationToProjectSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = OrganisationInProject
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    organisations = ProjectOrganisatiionSerailizer(many=True)

    class Meta:
        model = Project
        fields = '__all__'

    def create(self,validated_data):
        orgs = validated_data.pop('organisations')
        project = super().create(validated_data)
        for org in orgs:
            OrganisationInProject.objects.create(project=project,**org)
        return project

        

    
class ProjectAdminSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProjectAdmin
        fields = '__all__'

    

class UserProjectSerailizer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model =  UserProject
        fields = '__all__'


class ProjectOrganisationSerializer(serializers.ModelSerializer):
    organisation = OrganisationSerializer()
    class Meta:
        model = OrganisationInProject
        fields = ["organisation",]    

class ProjectDetailSerializer(ProjectSerializer):
    admins = ProjectAdminSerializer(many=True)
    users = UserProjectSerailizer(many=True)
    organisations = ProjectOrganisationSerializer(many=True)



class ApproveProjectSerializer(serializers.Serializer):
    user = serializers.StringRelatedField(read_only=True)
    project = serializers.StringRelatedField(read_only=True)
    status = serializers.CharField(read_only=True)

    def update(self, instance, validated_data):
        instance.approveRequest(user=validated_data['user'])
        return instance




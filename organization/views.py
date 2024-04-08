from os import stat
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework import response
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.generics import GenericAPIView
from django.core.exceptions import ObjectDoesNotExist

import organization

# Create your views here.
from .models import *
from .serializers import *



@api_view(['GET'])
@permission_classes([AllowAny])
def all_organizations(request):
    get_organizations = Organization.objects.all()
    if not get_organizations:
        return Response({"error":"No organizations"})
    serializers = OrganizationSerializer(get_organizations, many=True)
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_organization(request):
    if request.method == "POST":
        get_data = request.data
        try:
            get_organization = Organization.objects.filter(organization_name = get_data.get('organization_name')).first()
            if get_organization:
                return Response({"error":"Organization already exists"})
            else:
                org = OrganizationSerializer(data=get_data)
                if org.is_valid():
                    org.save()
                    return Response(org.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error":"something happened"}, status=status.HTTP_400_BAD_REQUEST)
        except Organization.DoesNotExist:
            return Response({"error":"organization doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_organization(request, pk):
    if request.method == "GET":
        get_organization = Organization.objects.filter(pk=pk).first()
        if not get_organization:
            return Response({"error":"Organization doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = OrganizationSerializer(get_organization)
            return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_organization_user(request, user_id):
    if request.method == "GET":
        get_organization = Organization.objects.filter(user = user_id)
        if not get_organization:
            return Response({"error":"Organization doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = OrganizationSerializer(get_organization, many=True)
            return Response(serializer.data)



@api_view(['PUT'])
@permission_classes([AllowAny])
def update_organization(request, pk):
    if request.method == "PUT":
        data = request.data
        get_organization = Organization.objects.filter(pk=pk).first()
        if not get_organization:
            return Response({"error":"Organization doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        serializers = OrganizationSerializer(get_organization, data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response({"error":"fileds wrong"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_organization(request, pk):
    get_organization = Organization.objects.filter(pk=pk).first()
    if not get_organization:
        return Response({"error":"Organization doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
    get_organization.delete()
    return Response({"message":"Organization deleted"})



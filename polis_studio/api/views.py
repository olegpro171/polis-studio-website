from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

import projects.models as models
import api.serializers as serializers


class ProjectView(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permissions = [AllowAny, ]
    pagination_class = None

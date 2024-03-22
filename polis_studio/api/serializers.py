from django.db import transaction
from drf_extra_fields.fields import Base64ImageField

from rest_framework import serializers

import polis_studio.constant_values as constants
import projects.models as models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ['id', 'name', 'slug', 'year', 'info', 'description']

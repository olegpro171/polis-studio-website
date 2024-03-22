from django.urls import include, path
from rest_framework.routers import DefaultRouter

import api.views as views

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('projects', views.ProjectView, basename='projects')

urlpatterns = [
    path('', include(router_v1.urls))
]

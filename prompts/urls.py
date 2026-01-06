from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'prompts', PromptViewSet)

urlpatterns = [
    path('', index),
    path('api/', include(router.urls))
]

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import UserApplySerializer
from .models import UserApplications

# Create your views here.

class UserApplicationViewSet(viewsets.ModelViewSet):
    queryset = UserApplications.objects.all()
    serializer_class = UserApplySerializer
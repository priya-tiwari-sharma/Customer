from .models import Profile
from .serializers import UserSerializers,ProfileSerializers
from rest_framework import viewsets
from django.contrib.auth.models import User
from detail.permissions import  IsOwner
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializers
    authentication_classes=[SessionAuthentication]
    permission_classes = [IsOwner]
  
    
  

class ProfileViewSet(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializers
    authentication_classes=[SessionAuthentication]
    permission_classes = [IsOwner]
    
    
    

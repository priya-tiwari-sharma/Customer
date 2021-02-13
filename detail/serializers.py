from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password   # for change in hash password
"""
we had to define similar fields on both Serializer and the Model class. 
We had to write codes for the same fields twice.
ModelSerializers can help solve that problem.
The serializer inspects the model and knows what fields to use and what their types are.
"""

# User Model
class ProfileSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(
            max_length=None, use_url=True
        )
    class Meta:
        model = Profile
        fields = ['id','image','state']

        
# Profile Model
class UserSerializers(serializers.ModelSerializer):
    profile=ProfileSerializers()
    

    class Meta:
        model = User
        fields = ['id','username','email','password','profile'] 
        validated_password=make_password

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user =User.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            password=make_password(validated_data["password"])
                       )
        #for pro_data in profile_data:
        Profile.objects.create(user=user,**profile_data)
        return user

    def update(self, instance, validated_data):
        user_id=User.objects.get(username=instance).id
        instance.username = validated_data.get('username', instance.username)
        instance.email= validated_data.get('email', instance.email)
        instance.password= make_password(validated_data.get('password', instance.password))
        instance.save()
        pf = validated_data.get('profile')
        profile_id=Profile.objects.get(user_id=user_id).id
       
        if profile_id:
            model = Profile.objects.filter(user_id=user_id)
            model.update(**pf)
        else:
            Profile.objects.create(user=user_id, **pf)
        return instance
            






    
    
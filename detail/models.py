from django.db import models
from django.contrib.auth.models import User


def nameFile(instance, filename):
    print("filename=======",filename)
    return filename

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    state=models.CharField(max_length=100)
    image=models.ImageField(blank=True,upload_to=nameFile,max_length=254)

    def __str__(self):
        return str(self.user)
    


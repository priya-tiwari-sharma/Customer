"""
http://polyglot.ninja/tag/django-rest-framework/


from django.shortcuts import render
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from detail.serializers import customerSerializers
from detail.models import Customer
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class CustomerAPI(View):

    def get(self,request,*args,**kwargs):
        #De-serialization(JSON-------------->PYTHON NATIVE DATATYPE--------------->COMPLEX DATATYPE)
        #                   --serialization--                     --jsonrenderer--  
        json_data=request.body           
        print("====",json_data)
        stream=io.BytesIO(json_data) #request.body return data in bytes but parse() take <class '_io.BytesIO'> object as an arguments
        pythondata=JSONParser().parse(stream)  # converting json ---->python native datatype
        username=pythondata.get('username',None)  
        if id is not None:
            customer=Customer.objects.get(username=username)                 # get data from database
            serializers=customerSerializers(customer)    # creating serializer object
            json_data=JSONRenderer().render(serializers.data) # render into json datatype
            return HttpResponse(json_data,content_type='application/json')
        customer=Customer.objects.all()     
        serializers=customerSerializers(data=customer,many=True)    
        json_data=JSONRenderer().render(serializers.data) 
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):  
         
        json_data=request.body           
        stream=io.BytesIO(json_data) 
        pythondata=JSONParser().parse(stream)
        print("pyth========",pythondata)
        serializers=customerSerializers(data=pythondata) 
        print("pyth========",serializers)
        if serializers.is_valid():
            serializers.save()
            res={'msg':'Successfully Register'}     # sending response after sucessfully insert data into database
            json_data=JSONRenderer().render(res)    
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializers.errors)        # if serializers.is_valid() not valid 
        return HttpResponse(json_data,content_type='application/json')


    

""" 


            





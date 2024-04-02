# Create your views here.
from django.shortcuts import render
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from testProject.models import CSVData
from testProject.services.staff import get_item_id, get_category, handle_uploaded_file

from .serializers import FilterSerializer, UploadCSVSerializer

class ImportCSVFile(APIView):
    def post(self, request):
        serializerCSVFile = UploadCSVSerializer(data=request.data)

        if serializerCSVFile.is_valid(raise_exception=True):
            csv_file = serializerCSVFile.validated_data['csv_file']
            print('csv_file=====>',csv_file)
            file = handle_uploaded_file(csv_file)
            return Response({"message": "File uploaded successfully"})
        if file == -1:
            return Response({"message": "Upload file is failed"})
        
        



class FilterView(APIView):
    def get(self, request):
        param_item_id = request.query_params.get('item_id')
        param_category = request.query_params.get('category')
    
        if param_item_id:
            staffFilter = get_item_id(param_item_id)
            return Response({"data": staffFilter})
        elif param_category:
            staffFilter = get_category(param_category)
            return Response({"data": staffFilter})
        else:
            return Response({"message": "No params are filled"})
        

class UpdateView(APIView):
    def put(self, request):
        param_item_id = request.query_params.get('item_id')
        instance = get_item_id(param_item_id)
        serializer = FilterSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data})

              
        
        
        
        
        
        
        


        
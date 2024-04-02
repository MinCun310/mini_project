import csv
from rest_framework import serializers

from testProject.models import CSVData

class CSVDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVData
        fields = '__all__'
        
class UploadCSVSerializer(serializers.Serializer):
    csv_file = serializers.FileField()
    
class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVData
        fields = '__all__'
        
        
        

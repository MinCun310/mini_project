import csv
from rest_framework.exceptions import NotFound

from testProject.models import CSVData
from testProject.serializers import CSVDataSerializer, FilterSerializer

def handle_uploaded_file(file):
    csv_data = []
    
    decoded_file = file.read().decode('utf-8').splitlines()

    csv_reader = csv.reader(decoded_file)
    
    i = 0
    for row in csv_reader:
        if(i==0):
            i+=1
            continue
        csv_data.append({
            'item_id': row[0],
            'japanese_name': row[1],
            'english_name': row[2],
            'category': row[3],
            'start_date': row[4],
            'end_date': row[5]
            })
    serializerCSVData = CSVDataSerializer(data=csv_data, many=True)
    
    if serializerCSVData.is_valid(raise_exception=True):
        serializerCSVData.save()
    else:
        return -1


def get_item_id(item):
    try:
        itemId = CSVData.objects.get(item_id=item)
        serialzer = FilterSerializer(itemId)
        return serialzer.data
    except Exception:
        raise NotFound("CSVData matching query does not exist.")
        

def get_category(category):
    try:
        category = CSVData.objects.filter(category=category)
        serialzer = FilterSerializer(category, many=True)
        return serialzer.data
    except Exception:
        raise NotFound("CSVData matching query does not exist.")

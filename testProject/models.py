from django.db import models

class CSVData(models.Model):
    item_id = models.CharField(max_length=100, unique=True)
    japanese_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    category = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
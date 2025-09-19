from django.db import models
from django.contrib import admin
class ABC_Company (models.Model):
    Car_Number=models.IntegerField(primary_key=True)
    Car_Model=models.CharField(max_length=30)
    Number_of_cars_sold=models.IntegerField()
    Year_Produced=models.DateField()
    Annual_Revenue=models.IntegerField()

class ABC_CompanyAdmin(admin.ModelAdmin):
    list_display=["Car_Number","Car_Model","Number_of_cars_sold","Year_Produced","Annual_Revenue"]

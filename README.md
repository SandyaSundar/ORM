# Ex02 Django ORM Web Application
## Date:15.09.2025 

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

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

admin.py

from django.contrib import admin
from .models import ABC_Company,ABC_CompanyAdmin
admin.site.register(ABC_Company,ABC_CompanyAdmin)
```



## OUTPUT

![alt text](<Screenshot (17).png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully

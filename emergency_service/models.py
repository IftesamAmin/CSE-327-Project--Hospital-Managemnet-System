from django.db import models

# Create your models here.
class EmergencyServiceProvider(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.


    this class used to create objects for database entry
    """
    e_provider_name=models.CharField(max_length=500)
    e_provider_password=models.CharField(max_length=500)
    e_services=models.CharField(max_length=1000)
    e_request_list=models.CharField(max_length=1000)

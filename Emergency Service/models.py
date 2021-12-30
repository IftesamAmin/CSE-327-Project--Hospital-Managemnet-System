from django.db import models

# Create your models here.
class Detail(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.


    this class used to create objects for database entry
    """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.IntegerField()
    status = models.CharField(max_length=50, default="register")



class FindAmbulance(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.


    this class used to create objects for database entry
    """
    username = models.CharField(max_length=30)
    ambulance_type = models.CharField(max_length=20)
    ambulance_number = models.CharField(max_length=30)


class GetOxygenCylinder(models.Model):
    """
    This class is extended from the Model class so it has all the functionality
    of the model class.


    this class used to create objects for database entry
    """
    username = models.CharField(max_length=30)
    cylinder_size = models.CharField(max_length=20)
    cylinder_number = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    patient_name = models.CharField(max_length=30)

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Data(models.Model):
	
	authar = models.ForeignKey(User, on_delete=models.CASCADE)
	User   = models.CharField(max_length= 50)
	ABBREVIATION_CHOICE = (
		('Mr', 'Mister'),
		('Mis', 'Misses'),
		('Dr', 'Doctor'),
		('Er', 'Engineer'),
		('Prof', 'Professor'),
		)
	salutation = models.CharField(max_length=30, choices=ABBREVIATION_CHOICE)

	CATEGRY_CHOICE =(
		('F', 'Female'),
		('M', 'Male'),
		)
	gender = models.CharField(max_length=10, choices=CATEGRY_CHOICE)
	birtday = models.DateField()
	address = models.CharField(max_length=255)


	"""docstring for Address"""

	def publish(self):
		self.published_date = timezone.now()
		self.save()
	    
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Person(models.Model):
	heading = models.CharField(max_length=100)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	User   = models.CharField(max_length= 50)
	# about = models.CharField(max_length=800)
	text = models.TextField(null=True)
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
	birthday = models.DateField()
	contact = models.CharField(max_length=12, null=True, blank=True)
	url = models.URLField(null=True)
	email = models.CharField(max_length=30)
	address = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='img', blank=True)


	"""docstring for Address"""

	def publish(self):
		self.published_date = timezone.now()
		self.save()
	    
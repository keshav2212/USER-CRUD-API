from django.db import models
class Member(models.Model):
	name=models.CharField(max_length=100)
	number=models.BigIntegerField()
	email=models.EmailField()
	date=models.DateField()
	is_hr=models.BooleanField()
	def __str__(self):
		return self.name
	
# Create your models here.

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class Member(models.Model):
	name=models.CharField(max_length=100)
	number=models.BigIntegerField()
	email=models.EmailField()
	date=models.DateField()
	is_hr=models.BooleanField()
	def __str__(self):
		return self.name

@receiver(post_save,sender=User)
def create_token(sender,instance=None,created=None,**kwargs):
	if created:
		Token.objects.create(user=instance)
# Create your models here.

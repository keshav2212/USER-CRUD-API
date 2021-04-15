from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver



@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
	print("Hello Keshav")
	print("sender:",sender)
	print("request:",request)
	print("user:",user)
	print(kwargs)


def logout_success(sender,request,user,**kwargs):
	print("Hello Keshav logout success")
	print("sender:",sender)
	print("request:",request)
	print("user:",user)
	print(kwargs)	
user_logged_out.connect(logout_success,sender=User)


@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
	print("Hello Keshav Wrong Crededentials")
	print("sender:",sender)
	print("request:",request)
	print("Crededentials:",credentials)
	print(kwargs)


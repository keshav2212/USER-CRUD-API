from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete, post_init,post_save,post_delete
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.models.signals import pre_migrate,post_migrate
from django.db.backends.signals import connection_created

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

@receiver(pre_save,sender=User)
def at_save_begin(sender,instance,**kwargs):
	print("Before Saving")
	print(sender)
	print(instance)

@receiver(post_save,sender=User)
def at_save_done(sender,instance,created,**kwargs):
	if created:
		print("After Saving")
		print(created)
	else:
		print("Updated Successfully")
	print(sender)
	print(instance)

@receiver(pre_delete,sender=User)
def at_delete_begin(sender,instance,**kwargs):
	print("Before Deleting")
	print(sender)
	print(instance)

@receiver(post_delete,sender=User)
def at_delete_end(sender,instance,**kwargs):
	print("After Deleting")
	print(sender)
	print(instance)


# @receiver(request_started)
# def at_request_started(sender,environ,**kwargs):
# 	print("Request Started")
# 	print(sender)
# 	print(environ)

# @receiver(request_finished)
# def at_request_ended(sender,**kwargs):
# 	print("Request Ended")
# 	print(sender)

# @receiver(got_request_exception)
# def at_request_exception(sender,request,**kwargs):
# 	print("After Exception")
# 	print(sender)


@receiver(pre_migrate)
def before_migration(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
	print("Before Migrations")
	print("Sender:",sender)
	print("App_Config",app_config)
	print("verbosity:",verbosity)
	print("interactive:",interactive)
	print("using:",using)
	print("plan:",plan)
	print("apps:",apps)


@receiver(post_migrate)
def after_migration(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
	print("At Migration Flush")
	print("Sender:",sender)
	print("App_Config",app_config)
	print("verbosity:",verbosity)
	print("interactive:",interactive)
	print("using:",using)
	print("plan:",plan)
	print("apps:",apps)

# @receiver(connection_created)
# def conncection_establish(sender,connection,**kwargs):
# 	print("Connection Intialized")
# 	print(sender)
# 	print(connection)

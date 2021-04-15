from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

#@method_decorator(csrf_exempt,name='dispatch')
class CustomAuthToken(ObtainAuthToken):
	def post(self,request,*args,**kwargs):
		serializer=self.serializer_class(data=request.data,context={'request':request})
		serializer.is_valid(raise_exception=True)
		user=serializer.validated_data['user']
		token,created=Token.objects.get_or_create(user=user)
		return Response({
		'token':token.key,
		'User':user.pk,
		'Email':user.email,
		})
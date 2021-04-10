from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io
from .models import Member
from django.utils.decorators import method_decorator
from .serializer import MemberSerializer
@method_decorator(csrf_exempt,name='dispatch')
class home(View):
	def get(self,request):
		data=request.body
		stream=io.BytesIO(data)
		json_data=JSONParser().parse(stream)
		mem=""
		if(json_data['id']==None):
			mem=Member.objects.all()
			serializer=MemberSerializer(mem,many=True)
			return JsonResponse(serializer.data,safe=False)
		else:
			try:
				mem=Member.objects.get(id=json_data["id"])
				serializer=MemberSerializer(mem)
				return JsonResponse(serializer.data)
			except:
				return JsonResponse({'Error':"Invalid Id"})
	def post(self,request):
		data=request.body
		stream=io.BytesIO(data)
		json_data=JSONParser().parse(stream)
		serializer=MemberSerializer(data=json_data)
		if serializer.is_valid():
			serializer.save()
		else:
			return JsonResponse(serializer.errors)
		return JsonResponse({'Success':"Member Created Successfully"})
	def put(self,request):
		data=request.body
		stream=io.BytesIO(data)
		json_data=JSONParser().parse(stream)
		try:
			mem=Member.objects.get(id=json_data['id'])
		except:
			return JsonResponse({'Error':"Invalid Id"})
		serializer=MemberSerializer(mem,data=json_data,partial=True)
		if serializer.is_valid():
			serializer.save()
		else:
			return JsonResponse(serializer.errors)
		return JsonResponse({'Success':"Member Updated Successfully"})
	def delete(self,request):
		data=request.body
		stream=io.BytesIO(data)
		json_data=JSONParser().parse(stream)
		mem=""
		try:
			mem=Member.objects.get(id=json_data['id'])
		except:
			return JsonResponse({'Error':"Invalid Id"})
		mem.delete()
		return JsonResponse({'Success':"Member Deleted Successfully"})
# Create your views here.

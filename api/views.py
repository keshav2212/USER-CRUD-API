import io
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Member
from django.utils.decorators import method_decorator
from .serializer import MemberSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from time import sleep
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
@method_decorator(csrf_exempt,name='dispatch')
class home(View):
	def get(self,request):
		data=request.body
		try:
			stream=io.BytesIO(data)
			json_data=JSONParser().parse(stream)
		except:
			id=None
		mem=""
		if(id==None):
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

@method_decorator(csrf_exempt,name='dispatch')
class apifun(APIView):
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAdminUser]
	def get(self,request,pk=None,format=None):
		if pk is not None:
			try:
				mem=Member.objects.get(id=pk)
			except:
				return Response({"Error":"Invalid ID"},status=status.HTTP_400_BAD_REQUEST)
			serializer=MemberSerializer(mem)
			return Response(serializer.data)
		else:
			mem=Member.objects.all()
			serializer=MemberSerializer(mem,many=True)
			return Response(serializer.data)
	def post(self,request,format=None):
		serializer=MemberSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'Success':"Member Created Successfully"},status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	def put(self,request,pk,format=None):
		mem=Member.objects.get(id=pk)
		serializer=MemberSerializer(mem,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'Success':"Member Updated Successfully"})
		else:
			return Response(serializer.errors)
	def patch(self,request,pk,format=None):
		mem=Member.objects.get(pk=pk)
		serializer=MemberSerializer(mem,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'Success':"Member Updated Successfully"},status=status.HTTP_202_ACCEPTED)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self,request,pk,format=None):
		mem=Member.objects.get(id=pk)
		mem.delete()
		return Response({'Success':"Member Deleted Successfully"})

# Create your views here.

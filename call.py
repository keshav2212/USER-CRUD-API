import requests
import json
def get():
	url='http://127.0.0.1:8000/'
	print("Enter ID (default all): ")
	x=input()
	n=None
	try:
		n=int(x)
	except:
		pass
	data={
		'id':n
	}
	data=json.dumps(data)
	r=requests.get(url=url,data=data)
	print(r.json())
def post():
	url='http://127.0.0.1:8000/'
	print("Enter Name: ")
	name=input()
	print("Enter Number: ")
	number=input()
	print("Enter Email: ")
	email=input()
	print("Enter Date: ")
	date=input()
	print("Is Hr (default False): ")
	hr=bool(input())
	data={
		'name':name,
		'number':number,
		'email':email,
		'date':date,
		'is_hr':hr,
	}
	data=json.dumps(data)
	r=requests.post(url=url,data=data)
	print(r.json())
def put():
	url='http://127.0.0.1:8000/'
	print("Enter Id for which you want to update: ")
	id1=int(input())
	print("Enter Name: ")
	name=input()
	print("Enter Number: ")
	number=input()
	print("Enter Email: ")
	email=input()
	print("Enter Date: ")
	date=input()
	print("Is Hr (default False): ")
	hr=bool(input())
	data={
		'id':id1,
		'name':name,
		'number':number,
		'email':email,
		'date':date,
		'is_hr':hr,
	}
	data=json.dumps(data)
	r=requests.put(url=url,data=data)
	print(r.json())
def delete():
	url='http://127.0.0.1:8000/'
	print("Enter ID: ")
	n=int(input())
	data={
		'id':n
	}
	data=json.dumps(data)
	r=requests.delete(url=url,data=data)
	print(r.json())
while(1):
	print("1. GET")
	print("2. POST")
	print("3. PUT")
	print("4. DELETE")
	print("3. Exit")
	n=int(input())
	if(n==1):
		get()
	elif(n==2):
		post()
	elif(n==3):
		put()
	elif(n==4):
		delete()
	else:
		break
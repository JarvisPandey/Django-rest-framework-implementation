from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import query
from django.views.decorators.csrf import csrf_exempt
from . serializers import queryserializer


from rest_framework.parsers import JSONParser


class queryList(APIView):

	def get(self, request):
		query1=query.objects.all()
		print("hhhhhhhhhh      ",query1[0])
		serializer=queryserializer(query1, many=True)
		return JsonResponse(serializer.data, safe=False)

	def post(self, request):
		#o=JSONParser()
		#data= o.parse(request)
		serializer=queryserializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status=201)
		return JsonResponse(serializer.errors, status=400)


class queryputList(APIView):
	def get_object(self, request, id):
		try:
			return query.objects.get(id=id)
		except query.DoesNotExist as e:
			return JsonResponse({"query DoesNotExist"},status=404)

	def get(self, request, id=None):
		inst=self.get_object(id)
		serializer=queryserializer(query1, many=True)
		return JsonResponse(serializer.data, safe=False)

	def put(self, request, id=None):
		inst=self.get_object(id)
		serializer=queryserializer(inst, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status=201)
		return JsonResponse(serializer.errors, status=400)


	def delete(self, request, id=None):
		inst=self.get_object(id)
		inst.delete()
		return HttpResponse(status=204)

		
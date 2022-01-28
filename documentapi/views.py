from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from documentapi.models import Document
from documentapi.serializers import DocumentSerializer

from django.core.files.storage import default_storage


# Create your views here.

@csrf_exempt
def document_api(request, id=0):
    if request.method == 'GET':
        documents = Document.objects.all()
        documents_serializer = DocumentSerializer(documents, many=True)
        return JsonResponse(documents_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        documents_serializer = DocumentSerializer(data=department_data)
        if documents_serializer.is_valid():
            documents_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Document.objects.get(DepartmentId=department_data['DepartmentId'])
        documents_serializer = DocumentSerializer(department, data=department_data)
        if documents_serializer.is_valid():
            documents_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        department = Document.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)

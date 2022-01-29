import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from documentapi.models import Document
from documentapi.serializers import DocumentSerializer

from django.core.files.storage import default_storage

from documentapi.upload_file import upload
from istv_profiler.auth import auth


# Create your views here.

@csrf_exempt
def document_api(request, id=0):
    if request.method == 'GET':
        documents = {}
        if bool(request.GET.dict()):
            id = request.GET['q']
            documents = Document.objects.get(documentId=id)

        else:
            documents = Document.objects.all()
        documents_serializer = DocumentSerializer(documents)
        return JsonResponse(documents_serializer.data, safe=False)
    elif request.method == 'POST':
        username = auth(request)
        upload(request)
        document_data = json.loads(request.POST['document'])
        documents_serializer = DocumentSerializer(data=document_data)
        # documents_serializer.creator = username
        print(document_data)
        print(documents_serializer.is_valid())
        if documents_serializer.is_valid():
            documents_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        document_data = JSONParser().parse(request)
        print(document_data)
        document = Document.objects.get(documentId=document_data['id'])
        documents_serializer = DocumentSerializer(document, data=document_data)
        if documents_serializer.is_valid():
            documents_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        document = Document.objects.get(documentId=id)
        document.delete()
        return JsonResponse("Deleted Successfully", safe=False)

from django.urls import re_path
from documentapi import views

urlpatterns = [
    re_path('documents', views.document_api),
    re_path('documents/<str:id>', views.document_api),
]

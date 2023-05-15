from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse

from tickets.models import Organization
from tickets.serializers import AdminOrganization, Organization

def home(request):
    return HttpResponse('Hello World!')

class AdminOrganizationViewSet(View):
    
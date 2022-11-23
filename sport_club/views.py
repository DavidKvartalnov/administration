from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


class CustomerApiView(APIView):
    def get(self, request):
        custom = Customer.objects.all().values()
        return Response({
            "customer": list(custom)
        })

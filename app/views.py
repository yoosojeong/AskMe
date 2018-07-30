from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
import json

class UserBox(APIView):

    def put(self, request, format=None):
        
        json_str = (request.body).decode('utf-8')
        request_json = json.loads(json_str)

        models.UserBox(message=request_json['message'], creator=request_json['creator']).save()

        return Response(status=status.HTTP_204_NO_CONTENT)


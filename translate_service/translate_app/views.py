import os
import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import JsonResponse
from translate_app.request_chatgpt import request_chatgpt
from translate_app.mongodb import MongoDB
from datetime import datetime

# Create your views here.
class TranslateView(APIView):
    parser_classes = (MultiPartParser,FormParser, JSONParser)
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'translate': openapi.Schema(type=openapi.TYPE_STRING, description='Text you want to translate'),
                'field': openapi.Schema(type=openapi.TYPE_STRING, description='Field of the text you want to focus on'),
                'topic': openapi.Schema(type=openapi.TYPE_STRING, description='Topic of the text you want to focus on'),
                'fromlangue': openapi.Schema(type=openapi.TYPE_STRING, description='Language of the text you want to translate'),
                'tolangue': openapi.Schema(type=openapi.TYPE_STRING, description='Language you want to translate to'),
            }
        ),
        responses={200: "Success"},
        operation_description="API to AI translate text from one language to another",
    )
    @csrf_exempt
    def post(self, request):
        print(request.data)
        Translate = request.data.get('translate')
        field = request.data.get('field')
        topic = request.data.get('topic')
        fromlangue = request.data.get('fromlangue')
        tolangue = request.data.get('tolangue')

        if field is None or topic is None or field == "" or topic == "":
            field = "General"
            topic = "General"
        
        response = request_chatgpt(Translate, field, topic, fromlangue, tolangue)
  
        data_response = response["choices"][0]["message"]["content"]

        # save to mongodb
        mongodb = MongoDB()
        id_request = mongodb.insert_one({
            'translate': Translate,
            'field': field,
            'topic': topic,
            'fromlangue': fromlangue,
            'tolangue': tolangue,
            'translated_text': data_response,
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
            'likeorunlike': 0
        })

        return JsonResponse({
            'response': data_response,
            "id_request": str(id_request)
        })

class GetTranslateView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id_request': openapi.Schema(type=openapi.TYPE_STRING, description='id of your requested translation'),
                }
            ),
            responses={200: "Success"},
            operation_description="Translate text using AI",
        )
    @csrf_exempt
    def post(self, request):
        id_request = request.data.get('id_request')
        print(id_request)
        mongodb = MongoDB()
        data = mongodb.find_one(id_request)
        if data:
            data['_id'] = str(data['_id'])
            data['created_at'] = str(data['created_at'])
            data['updated_at'] = str(data['updated_at'])

        return Response(data, status=status.HTTP_200_OK)
    
class UpdateTranslateView(APIView):
    parser_classes = (MultiPartParser,FormParser, JSONParser)
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_request': openapi.Schema(type=openapi.TYPE_STRING, description='Text you want to translate'),
                'likeorunlike': openapi.Schema(type=openapi.TYPE_INTEGER, description='Language of the text you want to translate'),
            }
        ),
        responses={200: "Success"},
        operation_description="API to AI translate text from one language to another",
    )
    
    @csrf_exempt
    def post(self, request):
        id_request = request.data.get('id_request')
        likeorunlike = request.data.get('likeorunlike')

        mongodb = MongoDB()
        data = mongodb.update_one(id_request, 'likeorunlike', likeorunlike)

        return Response("OK", status=status.HTTP_200_OK)

class SuggetsTranslateView(APIView):
    parser_classes = (MultiPartParser,FormParser, JSONParser)
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_request': openapi.Schema(type=openapi.TYPE_STRING, description='Text you want to translate'),
                'suggetion': openapi.Schema(type=openapi.TYPE_STRING, description='Text you want to suggetion'),
            }
        ),
        responses={200: "Success"},
        operation_description="API to sugggets result of translation",
    )
    
    @csrf_exempt
    def post(self, request):
        id_request = request.data.get('id_request')
        suggetion = request.data.get('suggetion')

        mongodb = MongoDB()
        data = mongodb.update_one(id_request, 'suggetion', suggetion)

        return Response("OK", status=status.HTTP_200_OK)
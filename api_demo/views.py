from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse

@api_view(['POST'])
def post_demo(request, name):
    print('request', request)
    return JsonResponse({
        'result':'success',
        'method':'post'
    })
@api_view(['GET'])
def get_demo(request, name):
    print('request',request,'\nname:', name)
    return JsonResponse({
        'result':'success',
        'method':'get'
    })
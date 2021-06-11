from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from django.http import HttpResponse,JsonResponse

@api_view(['POST'])
def post_demo(request):
    print('请求参数\n', request.query_params)
    return JsonResponse({
        'result':'success',
        'method':'Post'
    })

@api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
def get_demo(request):
    print('请求参数\n',request.query_params,'\nname:')
    return JsonResponse({
        'result':'success',
        'method':'Get'
    })
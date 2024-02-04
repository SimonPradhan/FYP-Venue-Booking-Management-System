from django.conf import settings
from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

@csrf_exempt
def khalti(request):
    token = request.POST.get('token')
    amount = request.POST.get('amount')
    payload = {
        "token":token,
        "amount":amount,
    }
    headers = {
        "Authorization": "Key {}".format(settings.KHALTI_SECRET_KEY)
    }
    try:
        response = requests.post(settings.KHALTI_VERIFY_URL,payload,headers=headers)
        if response.status_code == 200 :
            return JsonResponse({
                'status':True,
                'details':response.json(),
            })

        else:
            return JsonResponse({
                'status':False,
                'details':response.json(),
            })

    except requests.exceptions.HTTPError as e:
        return JsonResponse({
            'status':False,
            'details':str(e),
        })
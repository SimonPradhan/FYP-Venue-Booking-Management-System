from django.conf import settings
from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.core.mail import send_mail

@csrf_exempt
def khalti(request):
    data = json.loads(request.body)
    token = data.get('token')
    amount = data.get('amount')
    print(request.body)
    payload = {
        "token":token,
        "amount":amount,
    }
    print(payload)
    headers = {
        "Authorization": "Key {}".format(settings.KHALTI_SECRET_KEY)
    }
    try:
        response = requests.post(settings.KHALTI_VERIFY_URL,payload,headers=headers)
        if response.status_code == 200 :
            email = request.session.get('email', None)
            invoice(email,amount, data.get('product_name'), data.get('idx'))
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

def invoice(email, amount, product_name, idx):
    print(email, amount, product_name, idx)
    
    subject = 'EaseEvent Payment Invoice'
    message = f'Your amount for {product_name} is {amount}.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    # Print for testing, comment out in production
    print(subject, message, from_email, recipient_list)

    # Send the email using Gmail
    send_mail(subject, message, from_email, recipient_list, fail_silently=True)

    return Response({'status':True})
    

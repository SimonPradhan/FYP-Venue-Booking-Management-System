from django.conf import settings
from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.core.mail import send_mail
from venue import views


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
        "Authorization": "Key {}".format(settings.KHALTI_SECRET_KEY),
        'Content-Type': 'application/json'
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
    


# views.py


@csrf_exempt
def initiate_payment(request):
    if request.method == 'POST':
        url = "https://a.khalti.com/api/v2/epayment/initiate/"

        payload = json.dumps({
            "return_url": "http://example.com/",
            "website_url": "https://example.com/",
            "amount": "1000",
            "purchase_order_id": "Order01",
            "purchase_order_name": "test",
            "customer_info": {
                "name": "Ram Bahadur",
                "email": "test@khalti.com",
                "phone": "9800000001"
            }
        })
        headers = {
            'Authorization': 'test_secret_key_054bf433e1b343409cb7e79a087923ef',
            'Content-Type': 'application/json',
        }

        response = requests.post(url, headers=headers, data=payload)

        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Invalid request method."}, status=400)


from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

def invoice(email, total_amount, product_name, idx):
    # Calculate the amounts
    total_amount = float(total_amount)
    amount_paid = total_amount * 0.5
    remaining_amount = total_amount - amount_paid

    # Print the details for debugging
    print(email, total_amount, product_name, idx)

    # Compose the email subject and message
    subject = 'EaseEvent Payment Invoice'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    # Render the HTML template
    html_message = render_to_string('events/invoice_payment.html', {
        'idx': idx,
        'created_date': '2024-05-29',
        'due_date': '2024-06-29',
        'email': email,
        'product_name': product_name,
        'total_amount': total_amount,
        'amount_paid': amount_paid,
        'remaining_amount': remaining_amount,
    })

    # Create the email message
    email_message = EmailMultiAlternatives(subject, "", from_email, recipient_list)
    email_message.attach_alternative(html_message, "text/html")

    # Print the email details for testing (comment out in production)
    print(subject, html_message, from_email, recipient_list)

    # Send the email using the configured email backend
    email_message.send(fail_silently=True)

    # Return the response
    return Response({'status': True})
    

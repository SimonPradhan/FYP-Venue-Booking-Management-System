from django.shortcuts import render

# payments/views.py

import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

@csrf_exempt
def initiate_payment(request):
    if request.method == 'POST':
        # Replace 'LIVE_SECRET_KEY' with your live secret key for production
        khalti_secret_key = 'LIVE_SECRET_KEY'

        # Extract necessary data from the request
        data = json.loads(request.body)
        return_url = data.get('return_url', '')
        website_url = data.get('website_url', '')
        amount = data.get('amount', 0)
        purchase_order_id = data.get('purchase_order_id', '')
        purchase_order_name = data.get('purchase_order_name', '')
        customer_info = data.get('customer_info', {})
        amount_breakdown = data.get('amount_breakdown', [])
        product_details = data.get('product_details', [])

        # Khalti API endpoint
        khalti_api_url = 'https://khalti.com/api/v2/epayment/initiate/'

        # Prepare the payload
        payload = {
            'return_url': return_url,
            'website_url': website_url,
            'amount': amount,
            'purchase_order_id': purchase_order_id,
            'purchase_order_name': purchase_order_name,
            'customer_info': customer_info,
            'amount_breakdown': amount_breakdown,
            'product_details': product_details,
        }

        # Set up headers with authorization
        headers = {
            'Authorization': f'Key {khalti_secret_key}',
            'Content-Type': 'application/json',
        }

        # Make a POST request to initiate the payment
        response = requests.post(khalti_api_url, json=payload, headers=headers)

        # Process the response
        if response.status_code == 200:
            # Successful response
            data = response.json()
            payment_url = data.get('payment_url', '')
            return JsonResponse({'payment_url': payment_url})
        else:
            # Error handling
            error_data = response.json()
            return JsonResponse({'error': error_data}, status=response.status_code)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


def success_callback(request):
    # Handle success callback
    # Extract necessary parameters from the request and perform necessary actions
    return redirect('success_page_url')


def failure_callback(request):
    # Handle failure callback
    # Extract necessary parameters from the request and perform necessary actions
    return redirect('failure_page_url')

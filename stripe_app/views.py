from payment.settings import YOUR_DOMAIN, STIPE_SECRET_KEY
from django.views import View
from django.http import JsonResponse
import stripe
from django.shortcuts import render
import json

stripe.api_key = STIPE_SECRET_KEY

class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'success.html')

class CancelView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cancel.html')

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        try:
            product_data = json.loads(request.body)
            print(product_data)
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data':{
                            'currency' : 'inr',
                            'unit_amount' : product_data['price'],
                            'product_data': {
                                'name' : product_data['name']
                            }
                        },
                        'quantity':1
                    }
                ],
                payment_method_types=[
                'card',
                ],
                mode='payment',
                success_url = YOUR_DOMAIN + '/success',
                cancel_url = YOUR_DOMAIN + '/cancel',
            )
            return JsonResponse({
                'id' : checkout_session.id
            })
        except Exception as e:
            print(e)
            return JsonResponse({
                'error' : "Error"
            })

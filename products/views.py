from django.shortcuts import render
from payment.settings import STIPE_PUBLIC_KEY, PAYPAL_CLIENT_KEY, PAYPAL_SECRET_KEY, YOUR_DOMAIN, STIPE_SECRET_KEY, RAZORPAY_ID, RAZORPAY_SECRET_KEY
from django.views import View
from django.http import JsonResponse
import stripe
import json
import razorpay

stripe.api_key = STIPE_SECRET_KEY

razorpay_client = razorpay.Client(auth=(RAZORPAY_ID, RAZORPAY_SECRET_KEY))

class RazorpayCheckout(View):
  def post(self, request, *args, **kwargs):
    try:
      product_data = json.loads(request.body)
      data = { "amount": product_data['price'], "currency": "INR"}
      payment = razorpay_client.order.create(data=data)
      return JsonResponse({
        'response' : payment
      })
    except Exception as e:
      print(e)
      return JsonResponse({
        'error' : "Error"
      })

class StripeCheckout(View):
    def post(self, request, *args, **kwargs):
        try:
            product_data = json.loads(request.body)
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

class HomePage(View):
  def get(self, request, *args, **kwargs):
    context = {
      "title" : "Payment",
      "product" : {
        "name" : "Samsung Galaxy Flip Z",
        "price" : "84999.00"
      },
      'STRIPE_PUBLIC_KEY' : STIPE_PUBLIC_KEY,
      'PAYPAL_CLIENT_KEY' : PAYPAL_CLIENT_KEY,
      'PAYPAL_SECRET_KEY' : PAYPAL_SECRET_KEY,
      'RAZORPAY_KEY':RAZORPAY_ID,
      "payment_options" : [
        {
          "name" : "Stripe",
          "id" : "stripe-checkout-button"
        },
        {
          "name" : "PayPal",
          "id" : "paypal-checkout-button"
        },
        {
          "name" : "Razorpay",
          "id" : "razorpay-checkout-button"
        }
      ]
    }
    return render(request, 'index.html', context)

class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'success.html')

class CancelView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cancel.html')
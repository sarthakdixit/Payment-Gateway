from django.shortcuts import render
from payment.settings import STIPE_PUBLIC_KEY, PAYPAL_CLIENT_KEY, PAYPAL_SECRET_KEY
from django.views import View

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
      "payment_options" : [
        {
          "name" : "Stripe",
          "id" : "stripe-checkout-button"
        },
        {
          "name" : "PayPal",
          "id" : "paypal-checkout-button"
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
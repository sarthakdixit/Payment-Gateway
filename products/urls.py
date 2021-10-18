from django.urls import path, include
from .views import HomePage, SuccessView, CancelView, StripeCheckout, RazorpayCheckout

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('stripe/checkout', StripeCheckout.as_view(), name='stripe-checkout'),
    path('razorpay/checkout', RazorpayCheckout.as_view(), name='razorpay-checkout'),
    path('success', SuccessView.as_view(), name='success'),
    path('cancel', CancelView.as_view(), name='cancel')
]
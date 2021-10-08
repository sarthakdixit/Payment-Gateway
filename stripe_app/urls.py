from django.urls import path
from stripe_app.views import CreateCheckoutSessionView,SuccessView, CancelView

urlpatterns = [
    path('create-checkout-session', CreateCheckoutSessionView.as_view(), name='stripe-checkout-session'),
    # path('success', SuccessView.as_view(), name='stripe-success'),
    # path('cancel', CancelView.as_view(), name='stripe-cancel')
]
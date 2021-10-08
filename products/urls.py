from django.urls import path, include
from .views import HomePage, SuccessView, CancelView

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('success', SuccessView.as_view(), name='success'),
    path('cancel', CancelView.as_view(), name='cancel')
]
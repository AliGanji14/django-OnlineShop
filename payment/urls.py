from django.urls import path

from . import views

app_name = 'payment'
urlpatterns = [
    path('process/', views.payment_process_sandbox, name='payment_process'),
    path('callback/', views.payment_call_back_sandbox, name='payment_call_back'),
]

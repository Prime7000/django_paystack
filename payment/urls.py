

from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('verify/<str:ref>/', views.verify_payment, name='verify'),
   
]

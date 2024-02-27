

from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('details/<int:pk>', views.detail, name='details'),
    # path('place_order/<int:pk>', views.place_order, name='place_order'),
    path('place_order/', views.place_order, name='place_order'),

    path('', views.home, name = 'home')

]

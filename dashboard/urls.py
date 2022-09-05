from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('orders/',views.orders,name="orders"),
    path('updateorder/<str:pk>',views.orders,name="update_order"),
    path('stats/',views.stats,name="stats"),
    path('customers/',views.customers,name="customers"),
    path('register/',views.customer_reg,name="register"),
]
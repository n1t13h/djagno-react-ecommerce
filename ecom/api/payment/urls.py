from django.urls import path,include
from . import views
urlpatterns = [
    path('gettoken/<str:id>/<str:token>',views.generate_token,name='payment.token'),
    path('process/<str:id>/<str:token>',views.process_payment,name='payment.process'),
]
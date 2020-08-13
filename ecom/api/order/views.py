from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializer import OrderSerializer
from .models import Order
from django.views.decorators.csrf import csrf_exempt


def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        else:
            return False
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def addOrder(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse(
            {
                'error':'Not Logged In',
                'code':'403'
            }
        )
    if request.method == 'POST':
        user_id = id
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['products']
        total_pro = len(products.split(',')[:-1])
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
            return JsonResponse({
                'error':'User Does Not Exist'
            })

        order = Order(user,product_names=products,total_products=total_pro,total_amount=amount,transaction_id=transaction_id)
        order.save()
        return JsonResponse({
            'success':True,
            'error':False,
            'msg':'Order Placed Successfully'
        })


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
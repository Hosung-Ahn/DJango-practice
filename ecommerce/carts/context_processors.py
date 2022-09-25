from .models import CartItem
from .views import _cart_id

def cart_count(request) :
    cnt = 0
    try :
        products = CartItem.objects.filter(cart__cart_id = _cart_id(request))
        for product in products :
            cnt += product.quantity
    except :
        cnt = 0
    return dict(cnt=cnt)
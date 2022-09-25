from .models import CartItem
from .views import _cart_id

def cart_count(request) :
    cnt = 0
    products = CartItem.objects.filter(cart__cart_id = _cart_id(request))
    for product in products :
        cnt += product.quantity
    return dict(cnt=cnt)
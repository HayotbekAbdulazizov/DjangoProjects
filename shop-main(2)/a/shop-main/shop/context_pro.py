from .models import Category
from cart.models import Cart


def view_all(request):
	try:
		cart = Cart.objects.get(id=request.session.get('user_cart_id'))
	except:
		cart = {'status':'Savatcha topilmadi!'}
	print(cart)
	context = {
		'categories':Category.objects.all(),
		'cart':cart

	}
	return context
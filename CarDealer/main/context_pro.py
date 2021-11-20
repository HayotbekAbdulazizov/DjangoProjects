from .models import Category, Brand, Car


def view_all(request):
	print(request.user.id)
	context = {
		'categories':Category.objects.all(),
		'brands':Brand.objects.all(),
		'user_id ':request.user.id,
		'colors':Car.COLORS,
	}
	return context
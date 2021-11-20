from .models import Category, Brand


def view_all(request):
	print(request.user.id)
	context = {
		'categories':Category.objects.all(),
		'Brands':Brand.objects.all(),
		'user_id ':request.user.id
	}
	return context
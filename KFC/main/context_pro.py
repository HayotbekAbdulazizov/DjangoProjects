from .models import Category


def view_all(request):
	print(request.user.id)
	context = {
		'categories':Category.objects.all(),
	}
	return context
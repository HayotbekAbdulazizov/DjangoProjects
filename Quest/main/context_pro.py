from .models import Category, Tag, Quest

def view_all(request):
	print(request.user.id)
	context = {
		'Categories':Category.objects.all(),
        'Tags':Tag.objects.all(),
        'questions':Quest.objects.all().order_by('?')[:5]

	}
	return context
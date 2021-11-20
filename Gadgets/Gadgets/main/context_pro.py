from .models import Category, Tag, Gadget


def view_all(request):
    category = Category.objects.all()

    context = {
        'categories':category,
    }
    return context





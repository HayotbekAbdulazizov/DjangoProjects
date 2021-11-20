from .models import Book, Category


def view_all(request):
    context = {
        'categories':Category.objects.all(),
        'books_all':Book.objects.all()
    }
    return context
from .models import Rubrics 


def view_all(request):
    context = {
        'Rubrics':Rubrics.objects.all()
    }
    return context
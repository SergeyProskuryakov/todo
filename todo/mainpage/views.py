from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasks
from .models import Categories


# Create your views here.
def index(request):
    result = ''
    categories = ''
    for a in Categories.objects.all():
        categories += a.description
    # all_tasks = Tasks.objects.all()
    # for t in all_tasks:
    #     result += str(t)
    return render(
        request,
        'mainpage/index.html',
        {
            'Задачи': Tasks.objects.all(), 'Категории': categories
            # 'tasks_list': result
        }
    )

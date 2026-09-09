from django.shortcuts import render

def home(request):
    context = {
        'visitor': request.GET.get('name', 'guest')
    }
    return render(request, 'core/home.html', context)

def about(request):
    context = {
        'visitor': request.GET.get('name', 'stranger')
    }
    return render(request, 'core/about.html', context)

def projects(request):
    project_list = [
        {'name': 'Contact Book', 'status': 'Done'},
        {'name': 'Hello Django', 'status': 'Done'},
        {'name': 'Multipage Site', 'status': 'In progress'},
    ]
    return render(request, 'core/projects.html', {'projects': project_list})

def post_detail(request, post_id):
    context = {
        'post_id': post_id
    }
    return render(request, 'core/post_detail.html', context)
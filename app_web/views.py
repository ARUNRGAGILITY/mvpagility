from django.shortcuts import render

def web_home(request):

    context = {
        'page': 'web_home',
    }
    return render(request, 'app_web/web_home.html', context)
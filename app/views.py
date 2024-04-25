from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail


def index(request):
    info = Information.objects.last()
    hobby = Hobby.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.all() 
    clients = Client.objects.all()
    project = Project.objects.all()
    category = Category.objects.all()

    context = {
        'info': info, 
        'hobby': hobby, 
        'education': education, 
        'skills': skills,
        'project': project,
        'category': category,
        'clients': clients

    }
    return render(request, 'components/index.html', context)

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        try:
            send_mail(
                'New message from your portfolio',  
                f'Name: {fullname}\nEmail: {email}\nMessage: {message}', 
                'jearmsunaawan@gmail.com',  
                ['christianroy.mabilin04@gmail.com'],  
                fail_silently=False,
            )
            return HttpResponseRedirect('/')  
        except Exception as e:
            return HttpResponseRedirect('/')

    return HttpResponseRedirect('/')
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from .models import *


def index(request):

    global content
    course_category_obj = Course_Category.objects.all()

    content = {
        'course_category_obj': course_category_obj,
    }

    return render(request, 'index.html', context=content)


def course_informations(request, slug):

    fetch_dtls = Course_Category.objects.get(slug=slug)

    s_no = request.GET.get('serial_no')

    if s_no is None:
        s_no = 1
    try:
        video = Course_Information.objects.get(course=fetch_dtls, s_no=s_no)
        request.session['name'] = video.title
        print(request.session['name'])

    except:
        return redirect('home')
    context = {
        'fetch_dtls': fetch_dtls,
        'f': video,
        'content': content.get('course_category_obj')


    }

    return render(request, 'html_tutorial.html', context=context)


def testing_de(request, slug):

    c = request.session.get('name')
    return render(request, 'f.html', {'context': c, "slug": slug})

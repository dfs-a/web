from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    content = {

    }
    return render(request,'index.html',content)


def blog_add(request):
    blog = Blog.objects.all()

    if request.method == 'GET':
        return render(request, 'ZC.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        number = request.POST.get('number')
        blog = Blog(username=name,password=password,post_box=email,phone_number=number)
        blog.save()

        return render(request, 'DL.html', context={
            'blog':blog
        })


def blog_sj(request):
    blog = Blog.objects.all()
    print(blog)

# def blog_ym(request):
#     blog = Blog.objects.all()
#     return render(request, 'index.html', context={'blog':blog})



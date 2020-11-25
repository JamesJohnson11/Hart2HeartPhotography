from django.shortcuts import render
#from .models import Post, Gallery
#from django.utils import timezone
#from django.views.generic import TemplateView


def index(request):
    return render(request, 'index1.html')
'''
def services(request):
    return render(request, 'services.html')

def maternity(request):
    return render(request, 'maternity.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog.html', {'posts': posts})

def nature(request):
    return render(request, 'nature.html')

def children(request):
    return render(request, 'children.html')

def wedding(request):
    return render(request, 'wedding.html')


def test(request):
    return render(request, 'test.html')

'''
# Create your views here.

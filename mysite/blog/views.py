# Create your views here.

from blog.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    return render_to_response('blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:10]
    })

def view_post(request): 
    post1 = Blog.objects.all().filter(id=request.GET['id'])  
    return render_to_response('blog/view_post.html', {
        'post1':post1
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })

def form(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
                p=form.save()
                return HttpResponseRedirect('done')
    else:
        form=BlogForm()
    return render_to_response('blog/blog_form.html',{'form':form},context_instance=RequestContext(request))

def done(request):
    return render_to_response('blog/done.html', context_instance=RequestContext(request))


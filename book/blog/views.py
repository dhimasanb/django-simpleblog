from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def blogs(request):
    return render(request, 'blogs.html')

def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blog.html', { 'blog': blog })
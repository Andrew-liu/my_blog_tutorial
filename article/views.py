# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404

from django.contrib.syndication.views import Feed

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from article.models import Article
from article.models import Tag

from datetime import datetime


# Create your views here.
def home(request):
    posts = Article.objects.all()  #获取全部的Article对象
    paginator = Paginator(posts, 2) #每页显示两个
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
        tags = post.tag.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post, 'tags': tags})


def archives(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 
                                            'error' : False})

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def about_me(request) :
    return render(request, 'aboutme.html')

# def blog_search(request):
#     tags = Tag.objects.all()
#     if 'search' in request.GET:
#         search = request.GET['search']
#         blogs = Article.objects.filter(caption__icontains = search)
#         return render_to_response('blog_filter.html',
#             {"blogs": blogs, "tags": tags}, context_instance=RequestContext(request))
#     else:
#         blogs = Blog.objects.order_by('-id')
#         return render_to_response("blog_list.html", {"blogs": blogs, "tags": tags},
#             context_instance=RequestContext(request))

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')

class RSSFeed(Feed) :
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content

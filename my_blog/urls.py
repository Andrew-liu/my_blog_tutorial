from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.home'),
    url(r'^(?P<my_args>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^test/$', 'article.views.test'),
)


"""
修改下 index() 视图， 让它显示系统中最新发布的 5 个调查问题，以逗号分割并按发布日期排序：:

from django.http import HttpResponse

from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question for p in latest_poll_list])
    return HttpResponse(output)
"""
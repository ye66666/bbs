from django.conf.urls import patterns, include, url
from django.contrib import admin
from web import views
from web_chat import urls as chat_urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^chat/', include(chat_urls)),
    url(r'^category/(\d+)/$', views.category,name='category'),
    url(r'^article/(\d+)/$', views.article_detail,name='article_detail'),
    url(r'^account/logout/', views.acc_logout,name='logout'),
    url(r'^account/login/', views.acc_login,name='login'),
    url(r'^article/new/', views.new_article,name='new_article'),


    url(r'^$', views.index,name='index'),
)

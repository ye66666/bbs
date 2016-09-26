from django.conf.urls import patterns, include, url
from web_chat import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'dashboard/$', views.dashboard,name='web_chat'),
    url(r'contacts/$', views.contacts,name='load_contact_list'),
    url(r'msg/$', views.new_msg,name='send_msg'),
    url(r'msg/$', views.new_msg,name='get_new_msg'),
)

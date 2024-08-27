from django.conf.urls import include, url
from django.contrib import admin
from app01 import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'filesdemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^reg/', views.reg),
    url(r'^files/', views.file),
    url(r'^download/', views.download_view),
]

from django.views.static import serve
from .settings import MEDIA_ROOT, DEBUG

if DEBUG:
    urlpatterns += url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),

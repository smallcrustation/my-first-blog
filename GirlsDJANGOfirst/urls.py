"""
Definition of urls for GirlsDJANGOfirst.
"""

from django.conf.urls import include, url, patterns
from django.contrib.auth import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page':'/'}),
    url(r'', include('blog.urls')),
]

"""
Definition of urls for GirlsDJANGOfirst.
"""

from django.conf.urls import include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),

]

from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()
)

urlpatterns = patterns('',
    # Examples:
    url(r'^locations/', include('locations.urls')),
    url(r'^$', RedirectView.as_view(url="locations/")),
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

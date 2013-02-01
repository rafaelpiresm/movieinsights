from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movieinsights.views.home', name='home'),
    # url(r'^movieinsights/', include('movieinsights.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$', 'scripts.views.index'),
    (r'^scripts/search/$', 'scripts.views.search'),
    (r'^scripts/fullsearch/$', 'scripts.views.full_search'),
    (r'^scripts/(?P<script_id>(.*))$', 'scripts.views.details'),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

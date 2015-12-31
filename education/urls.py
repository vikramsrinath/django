from django.conf.urls import patterns, include, url
from django.contrib import admin
import school


urlpatterns = patterns('',
  url(r'^students/', include('school.urls')),
  url(r'^admin/', include(admin.site.urls)),
)

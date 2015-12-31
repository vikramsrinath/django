from django.conf.urls import patterns, url

from school import views

urlpatterns = patterns('',
  url(r'^$', views.student_list, name='student_list'),
  url(r'^new$', views.student_create, name='student_new'),
  url(r'^edit/(?P<pk>\d+)$', views.student_update, name='student_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.student_delete, name='student_delete'),

  url(r'^show_more$', views.student_show_more, name='student_show_more'),
)

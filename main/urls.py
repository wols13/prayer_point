from django .conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^sorted_by_category/$', views.sorted_by_category, name='Sorted by category'),
	url(r'^add_prayer_point/$', views.add_prayer_point, name='Add prayer point'),
	url(r'^prayer_point_by_category/$', views.prayer_point_by_category, name='prayer_point_by_category'),
]

from django .conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^sorted_by_scripture/$', views.sorted_by_scripture, name='Sorted by scripture'),
	url(r'^add_prayer_point/$', views.add_prayer_point, name='Add prayer point'),
	url(r'^prayer_point_by_scripture/$', views.prayer_point_by_scripture, name='prayer_point_by_scripture'),
	url(r'^number_of_chapters/$', views.number_of_chapters, name='number_of_chapters'),
	url(r'^get_scripture/$', views.get_scripture, name='get_scripture'),
]

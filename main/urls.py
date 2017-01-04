from django .conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^sorted_by_scripture/$', views.sorted_by_scripture, name='Sorted by scripture'),
	url(r'^sorted_by_category/$', views.sorted_by_category, name='Sorted by category'),
]

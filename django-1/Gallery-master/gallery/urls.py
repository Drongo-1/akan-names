from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search/', views.search_image, name='search_image'),
    url(r'^location/(?P<image_location>\d+)', views.location_filter, name='location_filter'),
    url(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.single,name = 'single')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from music import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('music.urls')),
    url(r'jsonmusic', views.AlbumList.as_view()),
    url(r'^xmlrpc/', views.RequestAPI, name='xmlrpc'),

]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
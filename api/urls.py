from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from api.views import ImagesView, ImagesUploadView, ImagesDetailsView

urlpatterns = [
    path('upload/', ImagesUploadView.as_view(), name='upload'),
    path('images/', ImagesView.as_view(), name='images'),
    path('images/<int:id>/', ImagesDetailsView.as_view(), name='id_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)